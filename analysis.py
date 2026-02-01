import pandas as pd

df = pd.read_csv("dataset_results.csv")

# See most frequent mistakes
mismatch = df[df["expected_action"] != df["predicted_action"]]

print("\n❌ Top action mismatches:\n")
print(mismatch[["expected_action","predicted_action"]].value_counts().head(10))

print("\n❌ Average severity difference:\n")
df["severity_diff"] = abs(df["expected_severity"] - df["predicted_severity"])
print(df["severity_diff"].describe())
