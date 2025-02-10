import sys
import os
import requests
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config import CURRENT_QUIZ_URL, HISTORICAL_QUIZ_URL, DATA_DIR

def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching data from {url}: {e}")
        return None

def save_data():
    # Fetch current quiz data
    current_quiz = fetch_data(CURRENT_QUIZ_URL)
    if current_quiz:
        current_quiz_path = os.path.join(DATA_DIR, "sample_current_quiz.json")
        with open(current_quiz_path, "w") as file:
            json.dump(current_quiz, file, indent=4)
        print(f"Saved current quiz data to {current_quiz_path}")
    else:
        print("Using existing sample_current_quiz.json file.")

    # Fetch historical quiz data
    historical_quiz = fetch_data(HISTORICAL_QUIZ_URL)
    if historical_quiz:
        historical_quiz_path = os.path.join(DATA_DIR, "sample_historical_quiz.json")
        with open(historical_quiz_path, "w") as file:
            json.dump(historical_quiz, file, indent=4)
        print(f"Saved historical quiz data to {historical_quiz_path}")
    else:
        print("Using existing sample_historical_quiz.json file.")

if __name__ == "__main__":
    os.makedirs(DATA_DIR, exist_ok=True)
    save_data()
