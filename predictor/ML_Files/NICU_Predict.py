import pandas as pd
import joblib
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load model and scaler
model = joblib.load(os.path.join(BASE_DIR, "Pragnancy_NICU_model.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "scaler.pkl"))

# Testing;
example = {
    "Maternal_Age": 19,   # younger age (risk factor)
    "Edinburgh_Postnatal_Depression_Scale": 20,  # high depression score
    "PROMIS_Anxiety": 25,  # high anxiety
    "Gestational_Age_At_Birth": 33,  # preterm (<37 weeks)
    "Birth_Length": 42,   # shorter than average
    "Birth_Weight": 1800,  # low birth weight
    "Threaten_Life": 1,   # yes
    "Threaten_Baby_Danger": 1,  # yes
    "Threaten_Baby_Harm": 0,
    "Income_Cleaned": 10000,  # lower income
    "Maternal_Education_encoded": 1,  # lower education
    "Year": 2023,
    "Month": 7,
    "DeliveryMode_Caesarean-section (c-section)": 1,  # C-section
    "DeliveryMode_Unknown": 0,
    "DeliveryMode_Vaginally": 0,
    "Language_mapped": 1,
    "NICU_missing_flag": 0,
}
def predict_nicu_stay(example):
    # Convert into DataFrame
    # ------------------------------
    X_new = pd.DataFrame([example])

    # Ensure same column order as training
    X_new = X_new[model.feature_names_in_]

    # ------------------------------
    # Scale only the required columns
    # ------------------------------
    cols_to_scale = [
        "Maternal_Age", "Edinburgh_Postnatal_Depression_Scale",
        "PROMIS_Anxiety", "Gestational_Age_At_Birth",
        "Birth_Length", "Birth_Weight", "Income_Cleaned"
    ]

    X_new[cols_to_scale] = scaler.transform(X_new[cols_to_scale])

    # Predict
    pred_class = model.predict(X_new)[0]
    pred_prob  = model.predict_proba(X_new)[0]
    class_prob = pred_prob[pred_class] * 100
    # print("Predicted class:", pred_class)   # 1 = did Stay in NICU, 0 = Not stay
    # print("Predicted probabilities:", class_prob,"%")
    # If your model returns probabilities for multiple classes, check all
    pred_prob_all = model.predict_proba(X_new)[0]  # Get probabilities for all classes
    print(f"All class probabilities: {pred_prob_all}")
    return pred_class, class_prob

print("Inside script")
pred_class, class_prob = predict_nicu_stay(example)
print(f"Predicted NICU Stay: {pred_class} with probability {class_prob:.2f}%")

print("Predicted Standardized Stress:", end=" ")
print(predict_nicu_stay(example))





def get_model_performance():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(BASE_DIR, "metrics.json"), "r") as f:
        metrics = json.load(f)   # loads into a Python dict
    return metrics


# Example usage
print("Model Performance Metrics:")
print(get_model_performance()['accuracy'])
print(get_model_performance()['precision'])
print(get_model_performance()['recall'])
print(get_model_performance()['f1'])

# This block will only run when executing this file directly (e.g. python titanic_predict.py)
if __name__ == "__main__":
    # test code (won’t run in Django)
    predict_nicu_stay(example)
    get_model_performance()