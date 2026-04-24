# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 21:05:03 2026

@author: Amadu
"""

from pipeline import run_pipeline
from config import DEFAULT_LOCATION_CONFIG

def main():
    df = run_pipeline(DEFAULT_LOCATION_CONFIG)

    if df is not None:
        df.to_csv("data/air_quality.csv", index=False)
        print("Data saved successfully!")

if __name__ == "__main__":
    main()