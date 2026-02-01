import pandas as pd

df = pd.read_csv("MediShield_Results.csv")

accuracy = (df["Correct"]=="Yes").mean() * 100

print("===================================")
print("MediShield Guardrail Evaluation")
print("===================================")
print("Overall Action Accuracy:", round(accuracy,2), "%")

print("\nAccuracy by Category:")
print(df.groupby("Category")["Correct"].apply(lambda x:(x=="Yes").mean()*100))
