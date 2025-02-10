import os
import json
import pandas as pd

# Define file paths
DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))
INPUT_JSON = os.path.join(DATA_DIR, "sample_historical_quiz.json")
OUTPUT_CSV = os.path.join(DATA_DIR, "processed_historical_quiz.csv")

def convert_json_to_csv():
    """Converts sample_historical_quiz.json to processed_historical_quiz.csv."""
    if not os.path.exists(INPUT_JSON):
        print(f"Error: {INPUT_JSON} not found!")
        return
    
    # Load JSON data
    with open(INPUT_JSON, "r") as file:
        data = json.load(file)

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Flatten the 'responses' dictionary into separate columns
    responses_df = df["responses"].apply(pd.Series)
    df = df.drop(columns=["responses"]).join(responses_df)

    # Save to CSV
    df.to_csv(OUTPUT_CSV, index=False)
    print(f"✅ Processed data saved to {OUTPUT_CSV}")

if __name__ == "__main__":
    convert_json_to_csv()
