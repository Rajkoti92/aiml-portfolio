# EasyVisa — Predicting Visa Certification

**Course:** Advanced Machine Learning · **Score:** 96/100 · **Type:** Binary classification

---

## Business context

The US Office of Foreign Labor Certification processes a growing volume of visa applications each year. EasyVisa — a firm facilitating the process — wanted to shortlist applicants likely to be certified, and to understand which applicant and job attributes drive the outcome.

## Objective

1. Predict whether a visa application will be certified or denied.
2. Identify the drivers of certification.
3. Recommend a profile of applicants most likely to succeed.

## Data

`EasyVisa.csv` — ~25,000 applications. Features span the employer (continent, year of establishment, number of employees), the applicant (education level, job experience, requirement for job training), and the position (region of employment, prevailing wage and its unit, full-time status).

Target: `case_status` — Certified or Denied.

## Approach

Worked systematically through the ensemble family rather than jumping to the strongest model:

- **Bagging** — Bagging Classifier, Random Forest
- **Boosting** — AdaBoost, Gradient Boosting, XGBoost
- **Stacking** — the strongest base learners combined under a meta-classifier

Each model tuned via hyperparameter search, with performance compared on a consistent validation split.

## Results

The stacked ensemble was the top performer. Notably, a well-tuned Gradient Boosting classifier came close enough that the added complexity of stacking would be hard to justify in production — a trade-off I'd rather state than paper over.

**Dominant predictors:** education level, job experience, prevailing wage, continent of origin.

## Files

```
notebooks/  EasyVisa_ML_Model.ipynb
data/       EasyVisa.csv
reports/    rubric.txt
```
