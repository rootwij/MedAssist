import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

# --- Load the dataset ---
data_path = os.path.join(os.path.dirname(__file__), "../data/symptoms.csv")
df = pd.read_csv(data_path)

# --- Split the dataset ---
X_train, X_test, y_train, y_test = train_test_split(df["text"], df["label"], test_size=0.2, random_state=42)

# --- Build pipeline ---
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression())
])

# --- Train the model ---
pipeline.fit(X_train, y_train)

# --- Evaluate performance ---
y_pred = pipeline.predict(X_test)
print("=== Classification Report ===")
print(classification_report(y_test, y_pred))

# --- Save the trained model ---
model_dir = os.path.join(os.path.dirname(__file__), "../models/")
os.makedirs(model_dir, exist_ok=True)
model_path = os.path.join(model_dir, "doctor_recommender_model.pkl")
joblib.dump(pipeline, model_path)

print(f"✅ Model saved at: {model_path}")