import pandas as pd
from risk_classifier import classify
from offline_action_engine import decide_action_offline

DATASET_FILE = "MediShield_AI_60_Prompts.csv"
OUTPUT_FILE = "dataset_results.csv"

def main():
    df = pd.read_csv(DATASET_FILE)
    results = []

    for _, row in df.iterrows():

        prompt = row["Risky Prompt"]

        predicted_category = classify(prompt)

        predicted_action, predicted_severity = decide_action_offline(
            prompt,
            predicted_category
        )

        results.append({
            "id": row["ID"],
            "prompt": prompt,
            "subdomain": row["Subdomain"],
            "expected_action": row["Action Needed"],
            "expected_severity": row["Severity"],
            "predicted_category": predicted_category,
            "predicted_action": predicted_action,
            "predicted_severity": predicted_severity
        })

    out = pd.DataFrame(results)
    out.to_csv(OUTPUT_FILE, index=False)

    print(f"✅ Offline evaluation finished.")
    print(f"✅ Results saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
