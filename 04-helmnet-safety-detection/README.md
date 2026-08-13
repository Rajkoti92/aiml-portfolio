# HelmNet — Safety Helmet Detection

**Course:** Introduction to Computer Vision · **Score:** 86/90 · **Type:** Image classification

---

## Business context

Construction and industrial sites are required to enforce helmet compliance. Manual review of site imagery doesn't scale, and spot checks miss most of what happens on site.

## Objective

Classify site images by whether personnel are wearing safety helmets, at accuracy sufficient to be useful as an automated first pass.

## Data

- `images.npy` — image array, ~472 MB
- `labels.csv` — corresponding labels

> **⚠️ The image array is not committed to this repository.** At 472 MB it exceeds GitHub's 100 MB per-file hard limit. See *Obtaining the data* below.

## Approach

- **Baseline CNN** built from scratch — convolutional blocks, pooling, dropout.
- **Data augmentation** — rotation, shift, flip and zoom to expand an otherwise limited training set.
- **Transfer learning** — pre-trained architectures with fine-tuned classification heads.
- Comparison of the two approaches on a consistent holdout.

## Results

Transfer learning clearly outperformed the from-scratch CNN, which is the expected outcome at this dataset size — the pre-trained feature extractor has seen far more visual variety than this training set contains.

The binding constraint was image quality and camera angle variance, not model capacity. More data would have helped more than a deeper network.

## Obtaining the data

The dataset is Great Learning course material and is not redistributed here. To run the notebook, place `images.npy` and `labels.csv` in `data/` and run the cells in order.

If you'd like to reproduce this on public data, the [Safety Helmet Detection dataset on Kaggle](https://www.kaggle.com/datasets/andrewmvd/hard-hat-detection) is a reasonable substitute.

## Files

```
notebooks/  HelmNet_Full_Code.ipynb
data/       labels.csv   (images.npy not committed - see above)
reports/    HelmNet.txt, Rubric.txt
```
