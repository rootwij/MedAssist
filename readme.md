# 🩺 MedAssist - Intelligent Healthcare Assistant

**MedAssist** is a smart, text-based healthcare assistant designed to help patients manage their health records, receive doctor recommendations, find nearby healthcare facilities, track medications, schedule appointments, and view personalized health insights.

This project was developed as part of an academic capstone to integrate **Natural Language Processing**, **Machine Learning**, and **API-driven architectures** into a real-world application.

---

## 🚀 Deployed Backend (FastAPI)
🔗 https://medassist-301f.onrender.com

✅ Visit `/docs` for API testing with Swagger UI.

---

## 🧩 Features

- **Symptom-Based Doctor Recommendation** (with ML model and confidence score)
- **Electronic Health Record (EHR) Summarization**
- **Symptom Logging and User History**
- **Frontend Integration** (compatible with external chat UIs)
- **Streamlit Test UI** for local testing

---

## 🏛️ Tech Stack

| Component    | Technology          |
|--------------|----------------------|
| Backend      | FastAPI (Python)      |
| Frontend (Demo) | Streamlit           |
| Machine Learning | Scikit-learn (Logistic Regression) |
| Database (Planned) | PostgreSQL / Firebase |
| Hosting      | Render.com            |
| APIs         | Google Maps, Twilio (Upcoming Modules) |

---

## 📂 Project Structure

```bash
MedAssist/
├── main.py                  # FastAPI server entrypoint
├── streamlit_app.py          # Streamlit-based frontend (optional testing)
├── app/
│   ├── api/routes.py         # API routes
│   ├── services/
│   │   ├── nlp_router.py     # NLP router + model prediction
│   │   ├── symptom_mapper.py # Rule-based symptom matching
│   │   ├── ehr.py            # EHR summarization logic
│   │   └── logger.py         # Symptom logging
├── models/
│   └── doctor_recommender_model.pkl # Trained ML model
├── data/
│   ├── symptoms.csv          # Training dataset
│   └── symptom_logs.csv      # Logs created after predictions
├── training/
│   └── train_doctor_model.py # ML training script
├── requirements.txt          # Python dependencies
└── .gitignore                # Git ignore file
