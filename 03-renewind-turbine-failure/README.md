# ReneWind — Predicting Wind Turbine Generator Failure

**Course:** Introduction to Neural Networks · **Score:** 97/100 · **Type:** Predictive maintenance

---

## Business context

ReneWind monitors wind turbine generators via sensor data. The economics are asymmetric and that asymmetry is the entire problem:

| Outcome | Cost |
|---|---|
| Inspection (false alarm) | Low |
| Repair before failure (true positive caught) | Medium |
| Replacement after failure (missed failure) | **High** |

A model optimised for accuracy will happily trade a missed failure for several avoided false alarms. That is exactly the wrong trade.

## Objective

Build a classifier that identifies generator failures from sensor readings, **optimised for recall** rather than accuracy.

## Data

`Train.csv` / `Test.csv` — 40 anonymised, ciphered sensor features. The target is heavily imbalanced: failures are rare, which is precisely why they're expensive.

## Approach

- **Missing value treatment** and feature scaling.
- **Imbalance handling** — compared SMOTE oversampling, random oversampling and undersampling.
- **Neural network architecture** — varied depth, width, dropout, batch normalisation and activation functions.
- **Metric selection** — recall as primary, with precision tracked to keep false alarms tolerable.

## Results

The tuned network on SMOTE-balanced data caught the large majority of true failures at a false-positive rate the business could absorb.

The interesting work was not architecture search. It was deciding the metric before training anything — a model with higher accuracy and lower recall would have looked better on paper and cost ReneWind more money.

## Files

```
notebooks/  renewind-neural-network.ipynb
            renewind-neural-network_old.ipynb   (earlier iteration, kept for comparison)
data/       Train.csv, Test.csv
reports/    Project_description.txt, rubric.txt
```
