# Simulated data pipeline for mental health AI
import pandas as pd

def load_data():
    return pd.read_json("data/mental_health_records.json")

def transform(data):
    data["text_length"] = data["notes"].apply(len)
    return data

def validate(data):
    assert "diagnosis" in data.columns
    assert all(data["text_length"] > 10)

if __name__ == "__main__":
    df = load_data()
    df = transform(df)
    validate(df)
    print("Pipeline executed successfully.")
