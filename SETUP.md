# Setup — moving files from Google Drive into this repo

Everything except the notebooks and datasets is already written. This is the
mechanical part: download from Drive, drop files into the matching folders, push.

## Step 1 — download from Drive

From `AI&ML - PG` in your Drive, download these files:

| Drive location | File | → goes to |
|---|---|---|
| `Machine Learning/Personal Loan Campaign/` | `MLS2_Decision_Tree_Personal_Loan.ipynb` | `01-personal-loan-campaign/notebooks/` |
| | `Loan_Modelling.csv` | `01-personal-loan-campaign/data/` |
| | `Machine Learning - Project-Support-Session...pdf` | `01-personal-loan-campaign/reports/` |
| `Advanced Machine Learning/EasyVisa/` | `EasyVisa_ML_Model.ipynb` | `02-easyvisa-visa-approval/notebooks/` |
| | `EasyVisa.csv` | `02-easyvisa-visa-approval/data/` |
| | `rubric.txt` | `02-easyvisa-visa-approval/reports/` |
| `neural networks/` | `renewind-neural-network.ipynb` | `03-renewind-turbine-failure/notebooks/` |
| | `Train.csv`, `Test.csv` | `03-renewind-turbine-failure/data/` |
| | `Project_description.txt`, `rubric.txt` | `03-renewind-turbine-failure/reports/` |
| `computer_vision/` | `HelmNet_Full_Code.ipynb` | `04-helmnet-safety-detection/notebooks/` |
| | `labels.csv` | `04-helmnet-safety-detection/data/` |
| | `HelmNet.txt`, `Rubric.txt` | `04-helmnet-safety-detection/reports/` |
| | ⚠️ `images.npy` (472 MB) | **DO NOT COMMIT** |
| `NLP_GenAI/NLP_GenAI/Graded_Project/` | `Full_Code_NLP_RAG_Project_Notebook (2).ipynb` | `05-medical-assistant-rag/notebooks/` |
| | `Business Context.docx`, `Rubric.docx` | `05-medical-assistant-rag/reports/` |
| | ⚠️ `medical_diagnosis_manual.pdf` | **DO NOT COMMIT** (third-party) |
| `Model Deployment/SuperKart_Project/` | `SuperKart_Model_Deployment_Project.ipynb` | `06-superkart-deployment/notebooks/` |
| | `SuperKart.csv` | `06-superkart-deployment/data/` |
| | `HF_Deployment_Guide.md` | `06-superkart-deployment/` |
| | `superkart_backend_files/*` | `06-superkart-deployment/backend/` |
| | `superkart_frontend_files/*` | `06-superkart-deployment/frontend/` |
| | ⚠️ `superkart_..._v1_0.joblib` (60 MB) | **DO NOT COMMIT** |

Rename the NLP notebook to `Full_Code_NLP_RAG_Project_Notebook.ipynb` (drop the `(2)`).

## Step 2 — clear notebook outputs (recommended)

Notebooks with embedded plot images are 1–3 MB each and produce unreadable diffs.
Two options:

**Keep outputs** (recruiters see the plots without running anything) — do nothing.
This is the better choice for a portfolio.

**Strip outputs** (clean diffs, small repo):
```bash
pip install nbstripout
nbstripout 0*/notebooks/*.ipynb
```

## Step 3 — verify nothing oversized is staged

```bash
find . -type f -size +50M -not -path "./.git/*"
```
Should return nothing. If it doesn't, that file needs to be in `.gitignore`.

## Step 4 — create the repo and push

```bash
cd aiml-portfolio
git init -b main
git add .
git status                # review before committing
git commit -m "Applied machine learning portfolio: six end-to-end projects"

# Create the repo on github.com/new as "aiml-portfolio" (public, no README/gitignore/licence)
git remote add origin https://github.com/Rajkoti92/aiml-portfolio.git
git push -u origin main
```

## Step 5 — finish the repo on GitHub

1. **Description:** `Six end-to-end ML projects — classification, neural networks, computer vision, RAG, and a deployed inference endpoint. From an 11-year data engineer.`
2. **Website:** your LinkedIn URL
3. **Topics:** `machine-learning` `deep-learning` `python` `scikit-learn` `tensorflow` `rag` `computer-vision` `nlp` `xgboost` `model-deployment` `data-science` `portfolio`
4. Confirm the README renders correctly.

## Step 6 — link it back

- Add the repo to your LinkedIn **Featured** section
- Add each project to your LinkedIn **Projects** section with this repo's URL
- Put the repo link in your LinkedIn About or Contact info

## Optional — host the large artefacts

`images.npy` and the SuperKart `.joblib` don't belong in git. Upload them to a
Hugging Face dataset/model repo and link from the project READMEs. Free, and it
signals familiarity with the ML deployment ecosystem.
