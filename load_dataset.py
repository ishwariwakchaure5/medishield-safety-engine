import pandas as pd

DATASET_PATH = "MediShield_AI_60_Prompts.csv"   # or 120 file

def load_dataset():
    df = pd.read_csv(DATASET_PATH)
    return df
