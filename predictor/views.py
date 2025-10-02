from django.shortcuts import render
from predictor.ML_Files.NICU_Predict import predict_nicu_stay, get_model_performance
from .forms import PregnancyForm
from django.http import JsonResponse
def homepage(request):
    new_data = {}
    prediction = None
    probability = None

    if request.method == "POST":
        form = PregnancyForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # Handle one-hot encoding for DeliveryMode
            delivery_mode = data['DeliveryMode']
            delivery_one_hot = {
                "DeliveryMode_Caesarean-section (c-section)": 1 if delivery_mode == "cesarean" else 0,
                "DeliveryMode_Vaginally": 1 if delivery_mode == "vaginal" else 0,
                "DeliveryMode_Unknown": 1 if delivery_mode == "unknown" else 0,
            }

            new_data = {
                "Maternal_Age": int(data['Maternal_Age']),
                "Edinburgh_Postnatal_Depression_Scale": int(data['Edinburgh_Postnatal_Depression_Scale']),
                "PROMIS_Anxiety": int(data['PROMIS_Anxiety']),
                "Gestational_Age_At_Birth": float(data['Gestational_Age_At_Birth']),
                "Birth_Length": float(data['Birth_Length']),
                "Birth_Weight": int(data['Birth_Weight']),
                "Threaten_Life": int(data['Threaten_Life']),
                "Threaten_Baby_Danger": int(data['Threaten_Baby_Danger']),
                "Threaten_Baby_Harm": int(data['Threaten_Baby_Harm']),
                "Income_Cleaned": int(data['Income_Cleaned']),
                "Maternal_Education_encoded": int(data['Maternal_Education_encoded']),
                "Year": int(data['Year']),
                "Month": int(data['Month']),
                **delivery_one_hot,
                "Language_mapped": int(data['Language_mapped']),
                "NICU_missing_flag": int(data['NICU_missing_flag']),
            }

            # Call your prediction function
            pred_class, pred_prob = predict_nicu_stay(new_data)
            prediction = int(pred_class)
            probability = float(pred_prob)
            print("Inside view function - Prediction:", prediction)
            print("Inside view function - Probability:", probability)

            return JsonResponse({
                "prediction": prediction,
                "probability": probability,  # This was None, now it will have the value
            })

        else:
            return JsonResponse({"error": "Form is not valid", "errors": form.errors}, status=400)
    else:
        form = PregnancyForm()



    various_metrics = get_model_performance()
    # Convert to percentage + round
    formatted_metrics = {
        key: f"{round(value * 100, 2)}" for key, value in various_metrics.items()
    }

    context = {
        "metrics": formatted_metrics,
        "prediction": prediction,
        "probability": probability,
        "form": form,

    }
    return render(request, "predictor/index.html", context)