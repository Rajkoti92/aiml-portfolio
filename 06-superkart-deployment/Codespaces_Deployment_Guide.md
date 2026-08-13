# SuperKart — GitHub Codespaces Deployment Guide

Everything is prepared. You only need this repository pushed to GitHub and ~10 minutes.

## Prerequisites (once)

1. The repository (including `SuperKart_Project/superkart_backend_files/` and
   `SuperKart_Project/superkart_frontend_files/`) is pushed to GitHub:

   ```bash
   git add .
   git commit -m "Add SuperKart deployment files (backend + frontend)"
   git push origin main
   ```

2. A GitHub account with Codespaces enabled (free tier is enough).

## Part 1 — Start a Codespace

1. Open the repository on GitHub → green **Code** button → **Codespaces** tab →
   **Create codespace on main**.
2. Wait for the Codespace to open in the browser (VS Code UI with a terminal).

## Part 2 — Backend (Flask API, Docker)

1. In the Codespace terminal, build and start the backend container:

   ```bash
   docker build -t superkart-backend ./SuperKart_Project/superkart_backend_files
   docker run -d --name superkart-backend -p 7860:7860 superkart-backend
   ```

2. Open the **Ports** tab (next to Terminal), find port **7860**, right-click →
   **Port Visibility → Public**.
3. Copy the **forwarded URL** — it looks like:
   `https://<codespace-name>-7860.app.github.dev`
4. Test it: open the URL in a browser — you should see
   *"Welcome to the SuperKart Sales Prediction API!"*

## Part 3 — Frontend (Streamlit, Docker)

1. In the same Codespace terminal, build and start the frontend container,
   passing the backend's forwarded URL from Part 2:

   ```bash
   docker build -t superkart-frontend ./SuperKart_Project/superkart_frontend_files
   docker run -d --name superkart-frontend -p 8501:8501 \
     -e SUPERKART_API_URL="https://<codespace-name>-7860.app.github.dev" \
     superkart-frontend
   ```

   (If you skip the `-e` flag, you can paste the backend URL into the app's sidebar instead.)

2. Ports tab → port **8501** → **Port Visibility → Public**.
3. Open the frontend's forwarded URL:
   `https://<codespace-name>-8501.app.github.dev`

## Part 4 — Test inference

- **Single (online) prediction:** fill in the form and click **Predict Sales**.
- **Batch prediction:** upload `SuperKart.csv` (the target column is ignored if present)
  and click **Predict for Batch**; download the predictions CSV.

## Part 5 — Finish the notebook

Paste the two forwarded URLs into the notebook's deployment markdown cells:

- Backend: `https://<codespace-name>-7860.app.github.dev`
- Frontend: `https://<codespace-name>-8501.app.github.dev`

## Notes & troubleshooting

- **Codespace URLs are ephemeral**: stopping/recreating the Codespace changes the
  `<codespace-name>` part. Restarting is two `docker start` commands
  (`docker start superkart-backend superkart-frontend`).
- **Port shows 502/504** → the container isn't running: check `docker ps -a` and
  `docker logs superkart-backend`.
- **Frontend can't reach backend** → port 7860 visibility isn't Public, or the URL
  in the sidebar has a typo/trailing spaces.
- **Docker build is slow the first time** — the scikit-learn/xgboost wheels are large;
  subsequent builds use the cache.
