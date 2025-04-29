
import joblib
import os

model_path = os.path.join(os.path.dirname(__file__), "../../models/doctor_recommender_model.pkl")
model = joblib.load(model_path)

def route_intent(user_input: str) -> str:
    input_lower = user_input.lower()
    if "summary" in input_lower:
        return "EHR_SUMMARY"
    elif any(word in input_lower for word in ["pain", "fever", "rash", "anxiety", "diabetes"]):
        try:
            probs = model.predict_proba([user_input])[0]
            top_class = model.classes_[probs.argmax()]
            confidence = probs.max()
            return f"You should consult a {top_class}. Confidence: {confidence:.2f}"
        except Exception:
            return "We couldn’t determine a suitable specialist for your symptoms."
    elif "hospital" in input_lower or "clinic" in input_lower:
        return "FIND_FACILITY"
    elif "remind" in input_lower:
        return "MEDICATION_TRACKER"
    elif "appointment" in input_lower:
        return "APPOINTMENT_SCHEDULER"
    elif "analytics" in input_lower:
        return "HEALTH_ANALYTICS"
    else:
        return "UNKNOWN"
