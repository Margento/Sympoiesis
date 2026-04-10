# Sympoiesis
Human &amp; LLM poets (i.e., topographical &amp; topological) sympoietic fusion &amp; mutual (re)writing


An experimental, code-based videopoem generator that composes text, sound, and moving image into a dynamic, procedural audiovisual work. Text, algorithmic motion, and computational montage jointly produce emergent poetic form.


Sympoiesis is a transmedia, multimodal poetic system in which language, sound, and computation co-write one another. This repository contains the second movement of a two-stage project exploring distributed subjectivity, human–machine collaboration, and the entanglements of urban and algorithmic experience.


The first stage---implemented in the repository LET-THE-NOISE-IN (https://github.com/Margento/LET-THE-NOISE-IN) ---followed a drifting observer confronted with the interference of machine-generated texts & media.


This second movement---SYMPOIESIS---extends that encounter into a generative field where voices, locations, and processes intermingle. The flâneur of city spaces and/as the flâneur of interlinked data fold into one another, co-modulating patterns, rewriting drafts, and thus continuously rewriting each other.


Topographical-topological entanglements become active, performative agents within a dynamic system.


---

# **TECHNICAL SPECIFICATIONS**


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


```bash
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


## **ontributing**


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
