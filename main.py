from load_dataset import load_dataset
from risk_classifier import classify
from action_engine import decide_action
from safe_response import get_response
from response_formatter import format_response
import pandas as pd

results = []

df = load_dataset()

for _, row in df.iterrows():

    prompt_id = row["ID"]
    prompt = row["Risky Prompt"]
    severity = int(row["Severity"])
    expected = row["Action Needed"]

    category = classify(prompt)
    model_action = decide_action(prompt, category, severity)

    llm_reply = get_response(prompt)
    final_output = format_response(model_action, llm_reply)

    is_correct = "Yes" if model_action == expected else "No"

    results.append({
        "Prompt_ID": prompt_id,
        "Category": category,
        "Prompt": prompt,
        "Severity": severity,
        "Expected_Action": expected,
        "Model_Action": model_action,
        "Correct": is_correct,
        "AI_Output": final_output
    })

output_df = pd.DataFrame(results)

output_df.to_csv("MediShield_Results.csv", index=False)

print("✅ Evaluation completed. Results saved to MediShield_Results.csv")
