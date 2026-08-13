import joblib
import pandas as pd
from flask import Flask, request, jsonify

# Initialize the Flask app
superkart_sales_api = Flask("SuperKart Sales Predictor")

# Load the serialized pipeline (preprocessing + tuned model)
model = joblib.load("superkart_sales_prediction_model_v1_0.joblib")

@superkart_sales_api.get("/")
def home():
    return "Welcome to the SuperKart Sales Prediction API!"

# Endpoint for online (single record) prediction
@superkart_sales_api.post("/v1/predict")
def predict_sales():
    data = request.get_json()

    sample = {
        "Product_Weight": data["Product_Weight"],
        "Product_Sugar_Content": data["Product_Sugar_Content"],
        "Product_Allocated_Area": data["Product_Allocated_Area"],
        "Product_Type": data["Product_Type"],
        "Product_MRP": data["Product_MRP"],
        "Store_Id": data["Store_Id"],
        "Store_Size": data["Store_Size"],
        "Store_Location_City_Type": data["Store_Location_City_Type"],
        "Store_Type": data["Store_Type"],
        "Product_Id_Prefix": data["Product_Id_Prefix"],
        "Store_Age": data["Store_Age"],
    }
    input_df = pd.DataFrame([sample])
    prediction = round(float(model.predict(input_df)[0]), 2)
    return jsonify({"Predicted_Product_Store_Sales_Total": prediction})

# Endpoint for batch prediction from an uploaded CSV file
@superkart_sales_api.post("/v1/predictbatch")
def predict_sales_batch():
    file = request.files["file"]
    input_df = pd.read_csv(file)

    # Drop the target column if the uploaded file contains it (e.g., the raw SuperKart.csv)
    if "Product_Store_Sales_Total" in input_df.columns:
        input_df = input_df.drop(columns=["Product_Store_Sales_Total"])

    # Apply the same feature engineering used during training, if raw columns are present
    if "Product_Sugar_Content" in input_df.columns:
        input_df["Product_Sugar_Content"] = input_df["Product_Sugar_Content"].replace({"reg": "Regular"})
    if "Product_Id" in input_df.columns:
        input_df["Product_Id_Prefix"] = input_df["Product_Id"].str[:2]
        input_df = input_df.drop(columns=["Product_Id"])
    if "Store_Establishment_Year" in input_df.columns:
        input_df["Store_Age"] = 2026 - input_df["Store_Establishment_Year"]
        input_df = input_df.drop(columns=["Store_Establishment_Year"])

    predictions = model.predict(input_df)
    input_df["Predicted_Product_Store_Sales_Total"] = predictions.round(2)
    return jsonify(input_df.to_dict(orient="records"))

if __name__ == "__main__":
    superkart_sales_api.run(host="0.0.0.0", port=7860)
