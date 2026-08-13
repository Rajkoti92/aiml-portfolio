import os

import pandas as pd
import requests
import streamlit as st

# Backend API base URL.
# Priority: the SUPERKART_API_URL environment variable, then the value entered in the sidebar.
# On GitHub Codespaces the backend's forwarded URL looks like:
#   https://<codespace-name>-7860.app.github.dev
DEFAULT_API_BASE = os.environ.get("SUPERKART_API_URL", "https://<codespace-name>-7860.app.github.dev")

st.set_page_config(page_title="SuperKart Sales Predictor", page_icon="🛒", layout="centered")

# Sidebar: lets you paste the backend's forwarded URL without editing code
st.sidebar.header("Backend Settings")
API_BASE = st.sidebar.text_input("Backend API URL", value=DEFAULT_API_BASE).rstrip("/")

st.title("🛒 SuperKart Sales Prediction App")
st.write(
    "Forecast the quarterly sales revenue of a product in a SuperKart outlet. "
    "Fill in the product and store details below, or upload a CSV for batch predictions."
)

# ---------------- Online prediction ----------------
st.subheader("Online Prediction")

col1, col2 = st.columns(2)

with col1:
    product_weight = st.number_input("Product Weight", min_value=1.0, max_value=30.0, value=12.5, step=0.1)
    product_sugar = st.selectbox("Product Sugar Content", ["Low Sugar", "Regular", "No Sugar"])
    product_area = st.number_input("Product Allocated Area (ratio)", min_value=0.0, max_value=1.0, value=0.06, step=0.01)
    product_type = st.selectbox("Product Type", [
        "Fruits and Vegetables", "Snack Foods", "Frozen Foods", "Dairy", "Household",
        "Baking Goods", "Canned", "Health and Hygiene", "Meat", "Soft Drinks",
        "Breads", "Hard Drinks", "Others", "Starchy Foods", "Breakfast", "Seafood"])
    product_mrp = st.number_input("Product MRP", min_value=1.0, max_value=300.0, value=147.0, step=0.5)
    product_prefix = st.selectbox("Product Category (Id prefix)", ["FD (Food)", "DR (Drinks)", "NC (Non-Consumable)"])

with col2:
    store_id = st.selectbox("Store Id", ["OUT001", "OUT002", "OUT003", "OUT004"])
    store_size = st.selectbox("Store Size", ["Small", "Medium", "High"])
    store_city = st.selectbox("Store Location City Type", ["Tier 1", "Tier 2", "Tier 3"])
    store_type = st.selectbox("Store Type", ["Supermarket Type1", "Supermarket Type2", "Departmental Store", "Food Mart"])
    est_year = st.number_input("Store Establishment Year", min_value=1980, max_value=2026, value=2005, step=1)

input_data = {
    "Product_Weight": product_weight,
    "Product_Sugar_Content": product_sugar,
    "Product_Allocated_Area": product_area,
    "Product_Type": product_type,
    "Product_MRP": product_mrp,
    "Store_Id": store_id,
    "Store_Size": store_size,
    "Store_Location_City_Type": store_city,
    "Store_Type": store_type,
    "Product_Id_Prefix": product_prefix.split(" ")[0],
    "Store_Age": 2026 - est_year,
}

if st.button("Predict Sales", type="primary"):
    try:
        response = requests.post(f"{API_BASE}/v1/predict", json=input_data, timeout=30)
        if response.status_code == 200:
            prediction = response.json()["Predicted_Product_Store_Sales_Total"]
            st.success(f"Predicted Product-Store Sales Total: **{prediction:,.2f}**")
        else:
            st.error(f"API error (status {response.status_code}). Please check the backend service.")
    except requests.exceptions.RequestException:
        st.error(
            "Could not reach the prediction API. Verify the backend URL in the sidebar, that the "
            "backend container is running, and that port 7860 is set to Public in the Ports tab."
        )

# ---------------- Batch prediction ----------------
st.subheader("Batch Prediction")
st.write("Upload a CSV with the same columns as the SuperKart dataset (Product_Id and Store_Establishment_Year are handled automatically).")

file = st.file_uploader("Upload CSV file", type=["csv"])
if file is not None and st.button("Predict for Batch", type="primary"):
    try:
        response = requests.post(f"{API_BASE}/v1/predictbatch", files={"file": (file.name, file, "text/csv")}, timeout=120)
        if response.status_code == 200:
            results = pd.DataFrame(response.json())
            st.write(f"Predictions for {len(results):,} rows (showing the first 50; download the full file below):")
            st.dataframe(results.head(50))
            st.download_button(
                "Download predictions as CSV",
                results.to_csv(index=False).encode("utf-8"),
                "superkart_predictions.csv",
                "text/csv",
            )
        else:
            st.error(f"API error (status {response.status_code}). Please check the backend service.")
    except requests.exceptions.RequestException:
        st.error(
            "Could not reach the prediction API. Verify the backend URL in the sidebar, that the "
            "backend container is running, and that port 7860 is set to Public in the Ports tab."
        )
