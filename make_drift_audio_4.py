#!/usr/bin/env python3
import os
import sys
import numpy as np
import librosa
import soundfile as sf
import random
import json

# --------------------------------------------------------
# DRIFT MIX FUNCTION (your code cleaned / robusted)
# --------------------------------------------------------


def drift_mix(file_list,
              output_file="drift_mix.wav",
              sr=48000,
              target_duration=(360, 449),
              overlap_range=(12, 24),
              fade_time=2.0,
              min_files=16,
              max_files=28,
              per_file_limit=(24, 36),
              second_pass_count=5,
              second_pass_resample=(8, 24)):
    """
    Create a drift mix from a list of audio files.
    
    Features:
    - Random selection of files (min_files to max_files)
    - Truncate / sample random slices per file
    - Crossfade overlapping files
    - Second pass: resample shortest files and mix at end
    """

    import random
    import numpy as np
    import librosa
    import soundfile as sf

    timeline = []    # list of dicts: file, start_time, end_time, mode, fragment
    current_time = 0

    random.shuffle(file_list)

    # Pick number of files to mix
    num_files = random.randint(min_files, max_files)
    selected = file_list[:num_files]

    print(f"Mixing {num_files} files:")
    for f in selected:
        print("  -", f)

    # Target output length
    max_len = random.randint(int(target_duration[0] * sr),
                             int(target_duration[1] * sr))

    output = np.zeros(1)
    used_segments = []  # Store metadata for second pass

    # -------------------------
    # FIRST PASS: initial mix
    # -------------------------
    for i, f in enumerate(selected):
        print(f"\nLoading {f} ...")
        try:
            a, orig_sr = librosa.load(f, sr=None, mono=True)
        except Exception as e:
            print(f"❌ Error loading {f}: {e} — skipping.")
            continue

        # Resample
        if orig_sr != sr:
            a = librosa.resample(a, orig_sr, sr)

        # Random truncate / sample
        max_piece = random.randint(int(per_file_limit[0] * sr),
                                   int(per_file_limit[1] * sr))
        if len(a) > max_piece:
            start = random.randint(0, len(a) - max_piece)
            a = a[start:start + max_piece]

        # Store segment metadata for second pass
        used_segments.append({
            "file": f,
            "length": len(a),
            "orig_sr": orig_sr
        })

        # First file: start output
        if i == 0:
            output = a
            continue

        old_length = len(output)

        # -------------------------
        # OVERLAP MIXING
        # -------------------------
        fade = int(fade_time * sr)
        overlap_len = random.randint(int(overlap_range[0] * sr),
                                     int(overlap_range[1] * sr))

        overlap_len = min(overlap_len, len(a), len(output))
        fade = min(fade, overlap_len)

        append_len = max(0, len(a) - overlap_len)
        out_len = len(output) + append_len
        out = np.zeros(out_len)
        out[:len(output)] = output

        start = len(output) - overlap_len

        fade_in = np.linspace(0, 1, fade)
        fade_out = np.linspace(1, 0, fade)

        out[start:start + fade] = (
            output[start:start + fade] * fade_out +
            a[:fade] * fade_in
        )

        remaining = a[fade:]
        dest_start = start + fade
        dest_end = min(dest_start + len(remaining), len(out))
        out[dest_start:dest_end] = remaining[:dest_end - dest_start]

        new_length = len(out)

        segment_start = max(0, old_length - overlap_len) / sr
        segment_end = new_length / sr

        timeline.append({
            "file": f,
            "start": segment_start,
            "end": segment_end,
            "type": "first_pass",
            "mode": random.choice(["topographical", "topological", "disruptive"]),
            "fragment_id": None
        })

        output = out

    # -------------------------
    # SECOND PASS: reuse shortest files with fresh slices
    # -------------------------
    print(f"\nStarting second pass using {second_pass_count} shortest files...")

    # Sort by length ascending
    used_segments.sort(key=lambda x: x["length"])
    second_pass_files = used_segments[:second_pass_count]

    old_length = len(output)

    for info in second_pass_files:
        fname = info["file"]
        print(f"Second-pass sample from: {fname}")

        # Reload original audio
        try:
            a2, orig_sr = librosa.load(fname, sr=None, mono=True)
        except Exception as e:
            print(f"❌ Could not reload {fname}: {e}")
            continue

        if orig_sr != sr:
            a2 = librosa.resample(a2, orig_sr, sr)

        # New random slice
        max_piece_2 = random.randint(int(second_pass_resample[0] * sr),
                                     int(second_pass_resample[1] * sr))
        if len(a2) > max_piece_2:
            start = random.randint(0, len(a2) - max_piece_2)
            a2 = a2[start:start + max_piece_2]

        # Mix at the end of current output
        fade = int(fade_time * sr)
        overlap_len = random.randint(int(overlap_range[0] * sr),
                                     int(overlap_range[1] * sr))
        overlap_len = min(overlap_len, len(a2), len(output))
        fade = min(fade, overlap_len)

        append_len = max(0, len(a2) - overlap_len)
        out_len = len(output) + append_len
        out = np.zeros(out_len)
        out[:len(output)] = output

        start = len(output) - overlap_len

        fade_in = np.linspace(0, 1, fade)
        fade_out = np.linspace(1, 0, fade)

        out[start:start + fade] = (
            output[start:start + fade] * fade_out +
            a2[:fade] * fade_in
        )

        remaining = a2[fade:]
        dest_start = start + fade
        dest_end = min(dest_start + len(remaining), len(out))
        out[dest_start:dest_end] = remaining[:dest_end - dest_start]

        new_length = len(out)

        segment_start = max(0, old_length - overlap_len) / sr
        segment_end = new_length / sr

        timeline.append({
            "file": fname,
            "start": segment_start,
            "end": segment_end,
            "type": "second_pass",
            "mode": random.choice(["topographical", "topological", "disruptive"]),
            "fragment_id": None
        })

        output = out

    # -------------------------
    # FINAL TRIM
    # -------------------------
    output = output[:max_len]

    print(f"\nFinal duration: {len(output)/sr:.2f} seconds")
    sf.write(output_file, output, sr)
    print(f"Saved drift mix to: {output_file}")

    return output_file, timeline

# --------------------------------------------------------
# Utility: gather audio from a folder
# --------------------------------------------------------
def list_audio_files(folder, exts=(".wav", ".mp3", ".m4a", ".flac", ".ogg")):
    return [
        os.path.join(folder, f)
        for f in os.listdir(folder)
        if f.lower().endswith(exts)
    ]

# --------------------------------------------------------
# MAIN when running as script
# --------------------------------------------------------
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:\n  python make_drift.py <input_folder> [output_file.wav]")
        sys.exit(1)

    input_folder = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "drift_mix.wav"

    files = list_audio_files(input_folder)

    print(f"Found {len(files)} audio files.")
    
    output_file, timeline = drift_mix(files, output_file)
    json.dump(timeline, open(output_file.replace(".wav",".json"),"w"), indent=2)