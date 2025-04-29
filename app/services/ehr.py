def generate_ehr_summary():
    patient_data = {
        "diagnoses": [
            {"condition": "hypertension", "date": "Feb 2024"},
            {"condition": "type 2 diabetes", "date": "Jan 2023"}
        ],
        "medications": [
            {"name": "Metformin", "active": True},
            {"name": "Lisinopril", "active": True}
        ],
        "last_checkup": "June 2024"
    }

    latest_diagnosis = patient_data["diagnoses"][0]
    active_meds = [med for med in patient_data["medications"] if med["active"]]
    summary = (
        f"You were last diagnosed with {latest_diagnosis['condition']} in {latest_diagnosis['date']}. "
        f"You are currently on {len(active_meds)} medications. "
        f"Last check-up was in {patient_data['last_checkup']}."
    )

    return summary