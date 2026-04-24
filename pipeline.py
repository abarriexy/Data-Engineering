# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 20:59:25 2026

@author: Amadu
"""

from ingest import fetch_locations
from transform import to_dataframe, clean_data

def run_pipeline(config): 
    raw = fetch_locations(config)
    df = to_dataframe(raw)
    df = clean_data(df)
    return df