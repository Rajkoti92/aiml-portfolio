# Finish the push — 3 commands

The repo at `D:\508bytes\Career\aiml-portfolio` is fully assembled and **all 34 files are already staged**. I couldn't run the commit itself: my sandbox mounts your drive without delete permission, so git left a stale `index.lock` behind and refuses to proceed.

Deleting that one file unblocks everything.

## Run these in PowerShell or Command Prompt

```cmd
cd /d D:\508bytes\Career\aiml-portfolio
del .git\index.lock
git commit -m "Applied machine learning portfolio: six end-to-end projects"
```

Then create the repo on GitHub and push:

```cmd
git remote add origin https://github.com/Rajkoti92/aiml-portfolio.git
git push -u origin main
```

Create `aiml-portfolio` at **https://github.com/new** first — public, and do **not** tick "Add a README", ".gitignore" or "licence" (all three already exist here and would conflict).

## Sanity check before pushing

```cmd
git log --oneline
git ls-files | find /c /v ""
```

Expect one commit and **34** files, ~26 MB total.

---

## What's in the commit

| Project | Notebook | Data |
|---|---|---|
| 01 Personal Loan Campaign | ✅ | ✅ Loan_Modelling.csv |
| 02 EasyVisa | ✅ | ✅ EasyVisa.csv |
| 03 ReneWind | ✅ | ✅ Train.csv, Test.csv |
| 04 HelmNet | ✅ | ✅ labels.csv (images.npy excluded) |
| 05 Medical Assistant (RAG) | ✅ | PDF excluded |
| 06 SuperKart | ✅ | ✅ SuperKart.csv + backend/frontend Docker files |

Plus: top-level README, six project READMEs, `.gitignore`, `requirements.txt`, MIT `LICENSE`, `Codespaces_Deployment_Guide.md`.

## Deliberately excluded

| File | Size | Why |
|---|---|---|
| `images.npy` | 472 MB | Exceeds GitHub's 100 MB hard limit |
| `superkart_..._v1_0.joblib` | 61 MB | Above the 50 MB warning; model artefacts don't belong in git |
| `medical_diagnosis_manual.pdf` | 19 MB | Third-party course material — don't republish |

Each project README explains how to obtain the missing file.

## Still missing from Downloads

These weren't in your Downloads folder, so their `reports/` folders are thin. Grab them from Drive whenever convenient — nothing is blocked without them:

- `rubric.txt` → `02-easyvisa-visa-approval/reports/`
- `rubric.txt` → `03-renewind-turbine-failure/reports/`
- `Rubric.txt` → `04-helmnet-safety-detection/reports/`
- `Rubric.docx` → `05-medical-assistant-rag/reports/`

## After the push — settings on GitHub

**Description:**
> Six end-to-end ML projects — classification, ensembles, neural networks, computer vision, RAG, and a containerised deployment. From an 11-year data engineer.

**Website:** `https://www.linkedin.com/in/rajakoti-vantari`

**Topics:** `machine-learning` `deep-learning` `python` `scikit-learn` `tensorflow` `rag` `computer-vision` `nlp` `xgboost` `docker` `model-deployment` `portfolio`

---

## One decision to make: your existing `ai_ml_course` repo

You already have **github.com/Rajkoti92/ai_ml_course**, which contains the SuperKart project — and its 61 MB `.joblib` **is** committed there. SuperKart now appears in both repos.

Three options:

1. **Archive `ai_ml_course`** (Settings → Archive this repository). Keeps the history, makes clear `aiml-portfolio` is the current one. *Simplest.*
2. **Delete it.** Clean, but you lose the deployment commit history — which is genuinely good evidence of debugging work.
3. **Leave both.** Duplicate SuperKart across two repos looks careless to anyone browsing your profile.

I'd archive it.
