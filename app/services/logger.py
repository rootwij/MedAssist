import csv
import os

def log_symptom_query(input_text, predicted_specialist, timestamp):
    log_path = os.path.join(os.path.dirname(__file__), "../../data/symptom_logs.csv")
    file_exists = os.path.exists(log_path)
    with open(log_path, mode='a', newline='', encoding='utf-8') as log_file:
        writer = csv.writer(log_file)
        if not file_exists:
            writer.writerow(["timestamp", "input_text", "predicted_specialist"])
        writer.writerow([timestamp, input_text, predicted_specialist])
