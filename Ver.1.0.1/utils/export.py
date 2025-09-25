import pandas as pd
import os

def save_export(df: pd.DataFrame):
    df.to_csv("exports/results.csv", index=False)

def log_diagnostic(message: str):
    with open("logs/diagnostics.log", "a") as f:
        f.write(message + "\n")
