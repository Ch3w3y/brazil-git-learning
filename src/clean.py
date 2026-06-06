"""Data cleaning helpers."""
import pandas as pd

def clean(df):
    df = df.fillna({"value": df["value"].median()})
    mean, std = df["value"].mean(), df["value"].std()
    return df[(df["value"] >= mean - 3*std) & (df["value"] <= mean + 3*std)]
