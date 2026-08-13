# Applied Machine Learning Portfolio

**Rajakoti Vantari** — Lead Data Engineer @ CBRE · Snowflake · dbt · Azure · AWS
[LinkedIn](https://www.linkedin.com/in/rajakoti-vantari) · [GitHub](https://github.com/Rajkoti92)

---

I've spent eleven years building the data layer — cloud warehouses, dimensional models, and the ELT pipelines that feed them. Six of those years were on Snowflake and Azure, most recently leading a multi-country European data platform.

This repository is the other half of that work: six end-to-end machine learning projects, taking problems from raw data through EDA, modelling, tuning, and — in one case — a deployed inference endpoint.

The through-line is deliberate. A model is only ever as good as the pipeline feeding it, and most ML projects stall in exactly the place a data engineer is trained to handle: the messy handoff between the warehouse and the model.

Completed as part of the **PG Program in AI & Machine Learning** (Great Learning / UT Austin McCombs).

---

## Projects

| # | Project | Problem type | Core techniques | Score |
|---|---------|--------------|-----------------|-------|
| 1 | [Personal Loan Campaign](./01-personal-loan-campaign) | Binary classification | EDA, Decision Trees, pruning, class imbalance | 60/60 |
| 2 | [EasyVisa](./02-easyvisa-visa-approval) | Binary classification | Bagging, Random Forest, AdaBoost, Gradient Boosting, XGBoost, Stacking | 96/100 |
| 3 | [ReneWind](./03-renewind-turbine-failure) | Predictive maintenance | Neural networks, SMOTE, recall-optimised tuning | 97/100 |
| 4 | [HelmNet](./04-helmnet-safety-detection) | Image classification | CNNs, transfer learning, data augmentation | 86/90 |
| 5 | [Medical Assistant](./05-medical-assistant-rag) | RAG / generative AI | Embeddings, vector search, retrieval-augmented generation | 109/110 |
| 6 | [SuperKart](./06-superkart-deployment) | Regression + deployment | Model packaging, Flask API, Docker, Codespaces | 89/90 |

---

## 1. Personal Loan Campaign — who actually converts?

**The problem.** AllLife Bank has a large base of liability customers (depositors) and a small base of borrowers. The previous campaign converted just over 9%. Marketing wanted to know which depositors to target next — and why.

**What I did.** Explored the drivers of conversion, engineered features around income, family size and education, then built and pruned a decision tree classifier. Pruning mattered more than model choice here: the unpruned tree memorised the training set and told the business nothing actionable.

**What came out.** Income, education level and family size dominate conversion probability. The resulting rules were simple enough for the marketing team to act on directly — which is the point of a decision tree, and the reason I didn't reach for something more exotic.

---

## 2. EasyVisa — predicting visa certification

**The problem.** The US Office of Foreign Labor Certification processes an increasing volume of visa applications each year. EasyVisa wanted a model to shortlist applicants likely to be certified, and to surface the factors that drive the decision.

**What I did.** Worked through the full ensemble family — bagging, Random Forest, AdaBoost, Gradient Boosting, XGBoost — then stacked the strongest performers. Hyperparameter tuning throughout, with careful attention to the class distribution.

**What came out.** Education level, job experience and prevailing wage were the dominant signals. The stacked ensemble outperformed any single model, though the margin over a well-tuned Gradient Boosting classifier was smaller than the extra complexity justified — a trade-off worth stating plainly rather than hiding.

---

## 3. ReneWind — predicting turbine failure before it happens

**The problem.** ReneWind collects sensor data from wind turbine generators. Replacing a component before failure is far cheaper than repairing after it, and vastly cheaper than a full replacement. The cost asymmetry is the whole problem.

**What I did.** Built neural network classifiers over 40 anonymised sensor features. Handled significant class imbalance with SMOTE and oversampling. Deliberately optimised for **recall** rather than accuracy — a missed failure costs an order of magnitude more than a false alarm, so a model with better accuracy and worse recall is the wrong model.

**What came out.** The tuned network caught the large majority of true failures at an acceptable false-positive rate. The interesting work here wasn't architecture — it was framing the metric correctly before training anything.

---

## 4. HelmNet — safety helmet compliance from images

**The problem.** Construction sites need to verify helmet compliance. Manual review doesn't scale.

**What I did.** Built CNN classifiers from scratch, then applied transfer learning from pre-trained architectures. Data augmentation to expand an otherwise limited training set.

**What came out.** Transfer learning substantially outperformed the from-scratch CNN, as expected with this dataset size. The practical constraint was image quality and angle variance rather than model capacity.

> **Note on data.** The image array for this project is ~472 MB and is not committed. See [the project README](./04-helmnet-safety-detection) for how to obtain it.

---

## 5. Medical Assistant — RAG over a clinical reference manual

**The problem.** Clinicians need fast, grounded answers from dense reference material. A general-purpose LLM will answer confidently and sometimes wrongly — unacceptable in a clinical context.

**What I did.** Built a retrieval-augmented generation pipeline over a medical diagnosis manual: document chunking, embedding generation, vector storage and similarity search, with retrieved context passed to the generation step. The retrieval layer is what keeps answers grounded in the source document rather than in the model's priors.

**What came out.** Chunking strategy mattered more than any other single choice — chunk boundaries that split a clinical procedure mid-way produced confidently wrong retrievals. This is the project closest to my day job: it is fundamentally a data pipeline problem wearing an AI hat.

> **Note on data.** The source reference PDF is third-party course material and is not redistributed here.

---

## 6. SuperKart — from notebook to deployed endpoint

**The problem.** SuperKart wanted store-level sales forecasts. A notebook that produces a good RMSE is not a forecast anyone can use.

**What I did.** Built and tuned the regression model, then took it the rest of the way: serialised the trained pipeline, wrote a Flask backend exposing a prediction endpoint, built a Streamlit frontend to consume it, containerised both with Docker, and deployed them via GitHub Codespaces with public port forwarding.

**What came out.** The modelling was the easy half. Dependency pinning, model artefact versioning and environment reproducibility took longer than training — which is the honest lesson of the project and the reason I care about it most.

See [`Codespaces_Deployment_Guide.md`](./06-superkart-deployment/Codespaces_Deployment_Guide.md) for the deployment walkthrough.

---

## Tech stack

**Languages** · Python, SQL
**Data** · pandas, NumPy
**Modelling** · scikit-learn, XGBoost, TensorFlow / Keras
**Imbalance** · imbalanced-learn (SMOTE)
**NLP / GenAI** · sentence-transformers, vector search, RAG
**Visualisation** · Matplotlib, Seaborn
**Deployment** · Flask, Streamlit, Docker, GitHub Codespaces, joblib

---

## Repository layout

```
aiml-portfolio/
├── 01-personal-loan-campaign/
│   ├── notebooks/          Jupyter notebook
│   ├── data/               dataset (or instructions to obtain it)
│   ├── reports/            problem statement, rubric
│   └── README.md
├── 02-easyvisa-visa-approval/
├── 03-renewind-turbine-failure/
├── 04-helmnet-safety-detection/
├── 05-medical-assistant-rag/
├── 06-superkart-deployment/
│   ├── backend/            Flask API (Docker) (Docker)
│   ├── frontend/           Streamlit UI (Docker)
│   └── ...
├── requirements.txt
└── README.md
```

---

## Running these locally

```bash
git clone https://github.com/Rajkoti92/aiml-portfolio.git
cd aiml-portfolio
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

Each project folder has its own README with the problem statement, approach, and any data-access notes.

---

## A note on scope

These are course projects, and I'd rather say so than dress them up. The datasets are curated and the problem statements are given. What they demonstrate is method: correct metric selection, honest evaluation, and — in the SuperKart case — the willingness to carry a model past the notebook and into something that actually serves requests.

The production-scale work is on my [LinkedIn](https://www.linkedin.com/in/rajakoti-vantari).

---

## Licence

Code is MIT licensed. Datasets and problem statements are the property of Great Learning and are included or referenced for educational purposes only.
