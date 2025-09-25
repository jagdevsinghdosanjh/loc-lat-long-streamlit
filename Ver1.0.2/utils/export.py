import pandas as pd
import os

def export_to_excel(df: pd.DataFrame, filename="results.xlsx"):
    df.to_excel(filename, index=False)


def save_export(df: pd.DataFrame):
    df.to_csv("exports/results.csv", index=False)

def log_diagnostic(message: str):
    with open("logs/diagnostics.log", "a") as f:
        f.write(message + "\n")
