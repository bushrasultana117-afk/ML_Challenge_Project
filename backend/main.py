from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib



# CREATING FASTAPI APP


app = FastAPI(
    title="SentinelAI API",
    description="AI-Powered Industrial Machine Health Monitoring API",
    version="1.0.0"
)



# LOADING MODEL


model = joblib.load(
    "sentinel_random_forest_pipeline.pkl"
)



# PYDANTIC MODEL


class MachineData(BaseModel):

    factory_name: str
    machine_id: str

    temperature: float
    vibration: float
    humidity: float
    pressure: float
    energy_consumption: float



# ROOT


@app.get("/")
def home():

    return {
        "message": "SentinelAI API is running "
    }



# MODEL STATUS


@app.get("/model-status")
def model_status():

    return {
        "model": "Random Forest",
        "status": "loaded",
        "features": [
            "temperature",
            "vibration",
            "humidity",
            "pressure",
            "energy_consumption"
        ]
    }



# GENERATING RECOMMENDATIONS


def generate_recommendations(data, prediction):

    recommendations = []

    if data.temperature > 80:

        recommendations.append(
            "🌡️ High temperature detected. "
            "Inspect the cooling system and temperature sensor."
        )

    if data.vibration > 1:

        recommendations.append(
            "📳 High vibration detected. "
            "Inspect the motor, bearings, and mechanical components."
        )

    if data.humidity > 80:

        recommendations.append(
            "💧 High humidity detected. "
            "Check the machine environment and ventilation."
        )

    if data.pressure > 150:

        recommendations.append(
            "🔧 High pressure detected. "
            "Inspect the pressure system and related components."
        )

    if data.energy_consumption > 300:

        recommendations.append(
            "⚡ High energy consumption detected. "
            "Check the machine load and energy efficiency."
        )

    # If no problems were found
    if not recommendations:

        if prediction == 0:

            recommendations.append(
                "✅ No immediate maintenance required. "
                "Machine is operating normally."
            )

        else:

            recommendations.append(
                "✅ No specific sensor issues detected. "
                "Continue regular machine monitoring."
            )

    return recommendations



# CREATING MACHINE HEALTH SCORE


def calculate_health_score(data, prediction):

    score = 100

    if data.temperature > 80:
        score -= 20

    if data.vibration > 1:
        score -= 25

    if data.humidity > 80:
        score -= 10

    if data.pressure > 150:
        score -= 15

    if data.energy_consumption > 300:
        score -= 15

    if prediction == 1:
        score -= 10

    return max(score, 0)



# PREDICT


@app.post("/predict")
def predict(data: MachineData):

   
    # CREATING INPUT DATA
   

    input_data = pd.DataFrame([{

        "temperature": data.temperature,

        "vibration": data.vibration,

        "humidity": data.humidity,

        "pressure": data.pressure,

        "energy_consumption": data.energy_consumption

    }])



    # MODEL PREDICTION
  

    prediction = int(
        model.predict(input_data)[0]
    )



    # CONFIDENCE
   

    probability = None

    if hasattr(model, "predict_proba"):

        probabilities = model.predict_proba(
            input_data
        )[0]

        probability = float(
            max(probabilities)
        )


   
    # STATUS
    

    if prediction == 1:

        status = "ANOMALY"

        risk_level = "CRITICAL"

    else:

        status = "NORMAL"

        risk_level = "LOW"


   
    # RECOMMENDATIONS
   

    recommendations = generate_recommendations(
        data,
        prediction
    )


    
    # HEALTH SCORE
 

    health_score = calculate_health_score(
        data,
        prediction
    )


    
    # RETURN RESULT
   

    return {

        "factory_name": data.factory_name,

        "machine_id": data.machine_id,

        "prediction": status,

        "risk_level": risk_level,

        "confidence": probability,

        "health_score": health_score,

        "recommendations": recommendations

    }