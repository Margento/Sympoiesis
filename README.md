
# Sympoiesis: A Generative Poetry Field

**Human & LLM poets (topographical & topological) in sympoietic fusion & mutual (re)writing**

An experimental, code-based videopoem generator that composes text, sound, and moving image into a dynamic, procedural audiovisual work. Text, algorithmic motion, and computational montage jointly produce emergent poetic form.

Sympoiesis is a transmedia, multimodal poetic system in which language, sound, and computation co-write one another. This repository contains the **second movement** of a two-stage project exploring distributed subjectivity, human–machine collaboration, and the entanglements of urban and algorithmic experience.

The first stage—implemented in [`LET-THE-NOISE-IN`](https://github.com/Margento/LET-THE-NOISE-IN)—followed a drifting observer confronted with the interference of machine-generated texts & media. This second movement extends that encounter into a generative field where voices, locations, and processes intermingle. The flâneur of city spaces and the flâneur of interlinked data fold into one another, co-modulating patterns, rewriting drafts, and continuously rewriting each other.

Topographical-topological entanglements become active, performative agents within a dynamic system.


---

## 🌐 Conceptual Framework (of the notebook https://github.com/Margento/Sympoiesis/blob/main/Margento_Sympoiesis_GitHub.ipynb) 

Sympoiesis treats poetic generation not as prompt-to-output translation, but as a **dynamic field of negotiation**. The system operates through a stateful, recursive loop where two distinct agencies continuously modulate one another:

- **The Topographical Flâneur** (poetic, bodily, city-driven, erotic desire)  
  Responds to affect, rhythm, humidity, exhaustion, and urban pressure. It translates sensation into form, letting desire deform syntax and bleed across languages.

- **The Topological Flâneur** (structural, algorithmic, recursive system logic)  
  Reads the poem as a network graph. It preserves patterns of recursion, density, and rupture, converting affect into topology and letting coherence emerge only as structural residue.

These voices do not synthesize; they **contaminate**. Their relative dominance is computed dynamically through a state vector comprising three scalar pressures:
- **Desire (D)**: Affective intensity, erotic charge, and semantic drift
- **Topography (T)**: Urban density, rupture ratio, recursive score, and circulation
- **Stability (S)**: Memory retention, agreement convergence, and temporal coherence

The field is modulated by a **Pareto-distributed noise signature** that occasionally injects heavy-tailed disruptions, mimicking creative leaps, accidents, or systemic failures. Text, audio, and video are sampled as *shards* from a multimodal corpus, weighted by structural distance and noise warping. When aesthetic agreement drops, the system triggers **temporal retroaction**: past poetic memories are rewritten, and FFmpeg montage commands are emitted to materialize the negotiated state into audiovisual form.

Rather than illustrating a poem, Sympoiesis reveals relationships through emergent behavior—a choreography of computational gesture and linguistic expression where city, body, memory, and algorithm co-produce a poem as a field in flux.

---

## ⚙️ Architecture & Pipeline

The core loop implements the following generative cycle:

```
field → noise → RAG → desire/topography → prompt → writer → convergence → retroaction
```

1. **State Extraction**: The current poem is parsed into a feature vector (`F_vec`) capturing syllable density, tempo, pacing variance, valence, arousal, energy, and temporal recursion scores.
2. **Noise Field Generation**: A Pareto-weighted noise signature is computed from historical profiles, media logs, and current D/T/S values. It warps semantic distance and register selection.
3. **Multimodal RAG Sampling**: Text, audio, and video shards are selected via noisy k-NN matching. Audio/video gestures (`RECUR`, `FAIL`, `DRIFT`, `SILENCE`, `APPEAR`) are inferred from text geometry and media metadata.
4. **Dual Flâneur Rendering**: Prompts are dynamically constructed from the field state, shard residues, and α-driven rhetorical regimes. LLMs (`gpt-4.1`, `qwen2.5-7b`) are selected stochastically.
5. **Convergence & Agreement**: Outputs are fused or allowed to converge based on an aesthetic agreement score. Low agreement triggers temporal retroaction, rewriting past stanzas.
6. **Media Emission**: FFmpeg filter graphs are generated from gesture metadata, producing temporal montage commands for audio/video extraction and concatenation.
7. **State Update**: Desire, topography, and stability are updated. Ghost shards (ignored fragments) are reinjected as distorted residues. The loop continues.

---

## 🚀 Quickstart

### 1. Clone & Prepare
```bash
git clone https://github.com/Margento/Sympoiesis.git
cd Sympoiesis
```

### 2. Install Dependencies
```bash
pip install numpy scipy regex openai huggingface_hub scikit-learn moviepy
```

### 3. Prepare Data & State
- Place your previous-stage outputs (`feature_history.pkl`, `noise_signature.pkl`, `profile_history.pkl`) in the working directory.
- Load your multimodal corpus (`asymptote_multilingual_cleaned_intermedia_analyses_stanzas_and_translations.json`) and audio/video analysis files.
- Set your API tokens (`YOUR_KEY`, `YOUR_TOKEN`) in the notebook.

### 4. Run the Generative Field
```python
# Initialize state from previous stage
state = initialize_state_from_previous_stage(seed_state)
states = [state]

# Run N steps of the sympoietic loop
run_sympoietic_field(state, range(0, N))
```

### 5. Output
- `margento_hk_sympoiesis_states_{step}.pkl` → Full system state logs
- `margento_hk_sympoiesis_noise_logs_{step}.pkl` → Noise signatures & α values
- Console output → FFmpeg montage commands for audio/video extraction
- Negotiated text → Appended to `text_history` in state logs

---

## 📦 Requirements & Setup

| Component | Purpose |
|-----------|---------|
| `numpy`, `scipy` | Feature distance, Pareto sampling, stability computation |
| `regex` | Unicode script detection, syllable approximation |
| `openai`, `huggingface_hub` | LLM routing (`gpt-4.1`, `qwen2.5-7b`) |
| `scikit-learn` | Cosine similarity for shard affinity |
| `pickle`, `json` | State serialization & corpus loading |
| `moviepy` (optional) | Downstream compositing/rendering |
| `ffmpeg` | Audio/video montage execution (emitted by pipeline) |

---

## 🛠️ Usage

### Notebook-Driven Workflow
1. Open `MARGENTO_Sympoiesis_Videopoem.ipynb`
2. Run cells sequentially: data loading → state initialization → field loop → FFmpeg emission
3. Monitor console for generated montage commands and voice-switch negotiations
4. Extract state logs for analysis or downstream rendering

### Programmatic Integration
```python
from sympoiesis.engine import run_sympoietic_field, initialize_state_from_previous_stage

state = initialize_state_from_previous_stage(seed_state)
states = run_sympoietic_field(state, range(0, 10))
```

---

## 📐 Technical Specifications (for the notebook https://github.com/Margento/Sympoiesis/blob/main/Margento_Sympoiesis_GitHub.ipynb) 

### Generative Core
- **State Vector**: `desire` (arousal/excess), `topography` (rupture/recursion/density), `stability` (drift/agreement)
- **Noise Model**: Pareto-distributed semantic drift + register warping + temporal jitter
- **RAG Sampling**: Noisy k-NN with structural distance warping, ghost shard reinjection, intermedia link triggering
- **Convergence**: Aesthetic agreement scoring with temporal retroaction & frozen-state destabilization
- **Media Emission**: FFmpeg filter graphs for audio/video temporal manipulation (trim, split, concat, atempo, setpts)

### Downstream Rendering (Optional)
The pipeline emits FFmpeg commands for structural montage. For final compositing, the repository supports:
- **Programmatic Text Animation**: Smooth Bézier-driven motion paths with parametric duration, opacity, easing, and scale
- **Generative Montage**: Automated assembly of text, background footage, and overlays via `CompositeVideoClip`
- **Audio Integration**: Synchronized text arrival, adjustable segment levels, full export pipeline
- **Export**: `final.write_videofile("sympoiesis_final.mp4", fps=24, codec="libx264", audio_codec="aac")`

---

## 🔗 Related Projects & Credits

- **LET THE NOISE IN** — [`https://github.com/Margento/LET-THE-NOISE-IN`](https://github.com/Margento/LET-THE-NOISE-IN)  
  A generative poetry engine that complements the aesthetic and technical approach of Sympoiesis.

- **Audio & Media Sources**  
  Freesound.org, Montreal Sound Map, live performance recordings © MARGENTO (Berlin 2008)

---

## 🤝 Contributing

Pull requests and experimental forks are welcome. Feel free to experiment with:
- Alternative corpus structures or embedding spaces
- New rhetorical regimes or α-modulation functions
- Different gesture inference thresholds or FFmpeg filter chains
- Audio-responsive or real-time streaming variants


---

# **TECHNICAL SPECIFICATIONS** (for the notebook https://github.com/Margento/Sympoiesis/blob/main/MARGENTO_Sympoiesis_Videopoem.ipynb)


# **Sympoiesis — A Generative Videopoem Engine**


This repository contains the full code used to generate the **Sympoiesis videopoem** (submitted to a literary journal, stay tuned), including modular text-animation functions, parametric Bézier-curve typography, layered video compositing, and audio-responsive behaviors.


---


## **Features**


* **Programmatic Text Animation**


  * Smooth Bézier-driven motion paths
 
    
  * Parametric control of duration, opacity, easing, scale
 
    
  * Modular helper functions for clip generation


* **Generative Montage**


  * Automated assembly of multiple video layers
 
    
  * Precise alignment of text, background footage, and overlays
 
    
  * Configurable scene timing for recombinable sequences


* **Audio Integration**


  * Audio tracks synchronized with text arrival and transitions
 
    
  * Adjustable audio levels per segment
 
    
  * Fully exportable final composite with sound


* **Video Export Pipeline**


  * Built on **MoviePy**
 
    
  * Support for HD output and multi-layer rendering
 
    
  * Notebook-driven workflow or script execution


---


## **How It Works**


Sympoiesis builds the videopoem in **three conceptual stages**:


### **1. Generate Text Clips**


The notebook defines a parametric function such as:


* `bezier_text_clip(text, mode, start, end, screen, audio_level)`
  which creates a timed text clip animated along a smooth Bézier path.
  

### **2. Compose Layers**

Clips are combined using `CompositeVideoClip` to create:


* floating animated texts

  
* footage or background imagery

  
* overlays, fades, masks, transitions

  

### **3. Export Final Montage**


The montage is rendered as a full composite:


```
python
final.write_videofile("sympoiesis_final.mp4", fps=24, codec="libx264", audio_codec="aac")
```


The result is a computationally generated videopoem whose timing, form, and spatial relationships arise sympoietically from the interplay of code and text.


---


## **Requirements**


* Python 3.9+

  
* MoviePy

  
* NumPy

  
* JSON

  
* (Optional) Jupyter Notebook for interactive execution

  

Install dependencies:


```
bash
pip install moviepy numpy
```

---


## **Usage**


### **Option A — Run the Notebook**


1. Open the `MARGENTO_Sympoiesis_Videopoem.ipynb` notebook.

   
3. Run all cells to generate the text clips and final composite.

   
5. Exported video will appear in the notebook’s working directory.

   

### **Option B — Use as a Python Module**


You can integrate the helper functions in `/src`:


```python


from src.text_clips import bezier_text_clip


from src.compositing import build_montage



clip = bezier_text_clip("example", mode="in", start=0, end=3)


video = build_montage([clip])


video.write_videofile("output.mp4")


```

---

## **Concept & Poetics**


Sympoiesis engages with the idea of *“making-with”*:

text, algorithm, motion, and time co-produce meaning.


Rather than illustrating a poem, the system reveals relationships through emergent behavior—-


a choreography of computational gesture and linguistic expression.


---


## **Related Projects**


* **LET THE NOISE IN** — [https://github.com/Margento/LET-THE-NOISE-IN](https://github.com/Margento/LET-THE-NOISE-IN)
  A generative poetry engine that complements the aesthetic and technical approach of Sympoiesis.


## **Contributing**


Pull requests and experimental forks are welcome.
Feel free to experiment with:


* alternative text sources

  
* different Bézier parameters

  
* new montage structures

  
* audio-responsive variations


---



## **Credits**


Audio files credited to https://freesound.org/ & https://www.montrealsoundmap.com/.


Excerpted music video © MARGENTO (live in Berlin 2008), https://www.youtube.com/watch?v=TXLbPj38MUY&list=RDTXLbPj38MUY&start_radio=1.
