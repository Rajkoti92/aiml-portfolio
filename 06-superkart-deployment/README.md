# SuperKart — Sales Forecasting, Containerised and Deployed

**Course:** Model Deployment · **Score:** 89/90 · **Type:** Regression + deployment

---

## Business context

SuperKart operates food marts and supermarkets across multiple cities and wants store-level sales forecasts to plan inventory and staffing.

A notebook with a good RMSE is not a forecast anyone can use. This project takes the model the rest of the way — into two Docker containers serving live requests.

## Objective

1. Build a regression model predicting product sales per store.
2. Package it as a serving artefact.
3. Deploy it as a containerised API with a working frontend.

## Data

`SuperKart.csv` — ~8,500 records covering product attributes (weight, sugar content, type, MRP, allocated shelf area) and store attributes (establishment year, size, city tier, type).

Target: `Product_Store_Sales_Total`.

## Architecture

```
┌──────────────────┐        POST /predict        ┌─────────────────┐
│  Streamlit UI    │ ──────────────────────────► │   Flask API     │
│  (frontend/)     │ ◄────────────────────────── │   (backend/)    │
│  Docker :7861    │        predicted sales      │   Docker :7860  │
└──────────────────┘                             └────────┬────────┘
                                                          │
                                              ┌───────────▼───────────┐
                                              │ sklearn Pipeline      │
                                              │ (preprocessing +      │
                                              │  trained regressor)   │
                                              │ .joblib, 61 MB        │
                                              └───────────────────────┘
```

Both services are independently containerised and deployed via GitHub Codespaces with public port forwarding. See [`Codespaces_Deployment_Guide.md`](./Codespaces_Deployment_Guide.md).

## Approach

**Modelling**
- EDA and feature engineering across product and store dimensions
- Regression models compared and tuned
- Entire preprocessing chain bundled into the sklearn `Pipeline` so inference is guaranteed to match training

**Deployment**
- Trained pipeline serialised with `joblib`
- Flask backend exposing a `/predict` endpoint, containerised on `python:3.11-slim`
- Streamlit frontend, separately containerised, supporting single and batch prediction
- Both deployed to GitHub Codespaces with public forwarded URLs

## What actually mattered

The modelling was the easy half.

The commit history on this project is mostly deployment: fixing the Docker base image from `python:3.9-slim` to `python:3.11-slim` after a dependency wouldn't build, pinning package versions after an environment drifted, and fixing a frontend segfault on batch prediction.

None of that is data science. All of it is why the thing works. The single most common failure mode in ML deployment is preprocessing drift — transformations applied during training that aren't identically applied at inference. Bundling the full preprocessing chain into the serialised pipeline is what prevents it, and it's the one design decision here I'd defend in any review.

If there's one project in this portfolio that reflects how I actually think about ML, it's this one.

## Files

```
notebooks/   SuperKart_Model_Deployment_Project.ipynb
backend/     Dockerfile, app.py (Flask API), requirements.txt
frontend/    Dockerfile, app.py (Streamlit), requirements.txt
data/        SuperKart.csv
Codespaces_Deployment_Guide.md
```

> **Model artefact not committed.** `superkart_sales_prediction_model_v1_0.joblib` is 61 MB — above GitHub's 50 MB warning threshold and poor practice to version in git. Regenerate it by running the notebook, or see the deployment guide.

## Running locally

```bash
# Backend
docker build -t superkart-backend ./backend
docker run -d -p 7860:7860 superkart-backend

# Frontend
docker build -t superkart-frontend ./frontend
docker run -d -p 7861:7861 superkart-frontend
```

The backend must be reachable before the frontend will return predictions.
