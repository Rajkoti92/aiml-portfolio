# Personal Loan Campaign — Targeting Depositors Who Convert

**Course:** Machine Learning · **Score:** 60/60 · **Type:** Binary classification

---

## Business context

AllLife Bank has a large base of liability customers (depositors) and a comparatively small base of borrowers. Growing the loan book means converting depositors — and the previous campaign converted just over 9% of those targeted.

The marketing team didn't want a black box. They wanted to know **which** depositors to target and **why**, in terms they could act on.

## Objective

1. Predict whether a liability customer will accept a personal loan.
2. Identify the customer attributes that drive that decision.
3. Produce rules the marketing team can apply directly.

## Data

`Loan_Modelling.csv` — 5,000 customers, 14 attributes covering demographics (age, experience, family size), financials (income, mortgage, average credit card spend), and existing relationships with the bank (securities account, CD account, online banking, credit card).

Target: `Personal_Loan` — whether the customer accepted the offer in the last campaign.

## Approach

- **EDA** — univariate and bivariate analysis, outlier treatment, correlation review. Established the class imbalance early (~9% positive) so it informed every later decision.
- **Feature preparation** — encoding, handling of the negative `Experience` values (a data quality issue worth catching rather than silently accepting).
- **Modelling** — Decision Tree classifier as the primary model, chosen deliberately for interpretability over raw performance.
- **Pruning** — pre-pruning via hyperparameter constraints and post-pruning via cost-complexity. This was the decisive step.

## Results

The unpruned tree achieved near-perfect training performance and generalised poorly — the textbook failure mode, and worth showing rather than hiding. The pruned tree traded a small amount of test performance for a model shallow enough to read off as business rules.

**Dominant predictors:** income, education level, family size.

## Why a decision tree

A gradient-boosted ensemble would have scored higher. It would also have been useless to the person who had to design the campaign. When the deliverable is a targeting rule rather than a scoring API, interpretability *is* the requirement.

## Files

```
notebooks/  MLS2_Decision_Tree_Personal_Loan.ipynb
data/       Loan_Modelling.csv
reports/    problem statement (PDF)
```
