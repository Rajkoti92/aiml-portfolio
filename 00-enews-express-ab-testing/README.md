# E-News Express: A/B Testing & Statistical Analysis

## Project Overview

E-News Express is an online news portal experiencing declining subscriber growth. The management suspects the current landing page design is not engaging enough. A new landing page was designed, and an **A/B testing experiment** was conducted to evaluate its effectiveness.

## Business Problem

Determine whether the new landing page design leads to:
- Higher user engagement (time spent on page)
- Better conversion rates (user subscribes)

## Dataset

- **Source:** A/B test experiment with 100 randomly selected users
- **Groups:** 50 control (old page) + 50 treatment (new page)
- **File:** `data/abtest.csv`

| Column | Description |
|--------|-------------|
| `user_id` | Unique visitor identifier |
| `group` | Control or treatment |
| `landing_page` | Old or new page version |
| `time_spent_on_the_page` | Duration in minutes |
| `converted` | Subscription conversion (yes/no) |
| `language_preferred` | English, Spanish, or French |

## Statistical Tests Performed

| # | Question | Test | α |
|---|----------|------|---|
| 1 | Do users spend more time on the new page? | Independent t-test (one-tailed) | 0.05 |
| 2 | Is the new page conversion rate higher? | Two-proportion z-test (one-tailed) | 0.05 |
| 3 | Does conversion depend on language? | Chi-square test of independence | 0.05 |
| 4 | Does time on new page vary by language? | One-way ANOVA | 0.05 |

## Key Concepts Applied

- Descriptive Statistics & Data Visualization
- A/B Testing Methodology
- Shapiro-Wilk Normality Test
- Levene's Test for Homogeneity of Variances
- Hypothesis Testing (t-test, z-test, Chi-square, ANOVA)

## Tools & Libraries

Python, Pandas, NumPy, SciPy, Statsmodels, Matplotlib, Seaborn

## Course

Applied Statistics — Great Learning PG Program in AI & ML
