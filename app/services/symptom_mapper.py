
SYMPTOM_SPECIALTY_MAP = {
    "chest pain": "Cardiologist",
    "headache": "Neurologist",
    "skin rash": "Dermatologist",
    "eye pain": "Ophthalmologist",
    "joint pain": "Orthopedic",
    "anxiety": "Psychiatrist",
    "fever": "General Physician",
    "diabetes": "Endocrinologist"
}

def recommend_specialist(symptom: str) -> str:
    for key in SYMPTOM_SPECIALTY_MAP:
        if key in symptom.lower():
            return f"You should consult a {SYMPTOM_SPECIALTY_MAP[key]}."
    return "Sorry, we couldn’t identify a relevant specialist."
