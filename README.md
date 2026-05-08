# Is Sleep Really Made of Discrete Stages?

Exploring why EEG-based models fail at the boundaries between Wake, N1, N2, N3, and REM.

---

## Overview

Sleep is typically described as a sequence of discrete stages—Wake, N1, N2, N3, and REM—each defined by characteristic patterns in EEG signals.

But the underlying brain activity is continuous.

This project investigates a simple question:

**Are sleep stages truly separable in EEG signals, or are some boundaries inherently ambiguous?**

Instead of focusing on overall accuracy, the analysis focuses on **where and why classification fails**.

---

## Key Idea

The central hypothesis is that errors in sleep-stage classification are not random.

If the signal does not clearly belong to a single stage, we expect:
- higher error rates near transitions
- uneven separability across stages

To test this, each EEG segment is categorized as:
- **Stable** — surrounding stages remain the same  
- **Transition** — stage changes nearby  

---

## Dataset

The analysis uses the **Sleep-EDF (Expanded)** dataset from PhysioNet.

- Overnight EEG recordings
- 30-second annotated epochs
- Sleep stages: Wake, N1, N2, N3, REM
- Single EEG channel (Fpz–Cz) used for simplicity

---

## Approach

- Extract time-domain and frequency-based features from EEG segments  
- Train a **Random Forest classifier** as a baseline model  
- Evaluate performance across:
  - single-subject setting  
  - multi-subject setting  
  - with and without normalization  

- Analyze results along two axes:
  - stable vs transition regions  
  - per-stage classification behavior  

---

## Key Findings

### 1. Transitions are consistently harder to classify

Across all settings:
- accuracy is higher in stable regions  
- accuracy drops near transitions  

---

### 2. Cross-subject variability matters—but does not explain everything

- Multi-subject performance drops significantly  
- Normalization improves accuracy  
- **But the transition gap persists**

---

### 3. Not all sleep stages are equally separable

- **Wake, N2** → relatively robust  
- **N3** → strong in stable regions, degrades near transitions  
- **REM** → moderately difficult  
- **N1** → consistently poorly classified  

---

### 4. N1 behaves more like a transition than a state

Even in stable regions:
- N1 shows very low accuracy  
- It overlaps with multiple stages  

This suggests that **N1 may not be a well-defined, separable state in EEG signals**

---

## Conclusion

The main limitation is not just the model.

It reflects a deeper mismatch:

> EEG signals are continuous, but sleep stages are discrete labels.

Near transitions, the signal may not correspond cleanly to a single stage.

This leads to **structured, predictable failure**, especially at stage boundaries.

---

## Broader Implication

This pattern extends beyond sleep analysis.

Many real-world systems:
- evolve continuously  
- are labeled discretely  

In such cases:
- errors are not random  
- they are concentrated at boundaries  

Understanding these limits is as important as improving model performance.

---

## Article

Full write-up available on Medium:

https://medium.com/@subhabrata.ganguli/is-sleep-really-made-of-discrete-stages-877e35635ec2
---

## Notes

- This project focuses on **analysis of failure**, not model optimization  
- The goal is to understand the **limits of the signal and labeling framework**  
