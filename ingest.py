# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 20:48:12 2026

@author: Amadu
"""

import requests
import pandas as pd

from config import BASE_URL, HEADERS


def fetch_locations(config):
    url = f"{BASE_URL}/locations"

    response = requests.get(url, headers=HEADERS, params=config)
    response.raise_for_status()

    data = response.json()
    results = data.get("results", [])

    if not results:
        print("No locations found. Check your config or API key.")
        return pd.DataFrame()

    df = pd.json_normalize(results)

    # Keep useful columns if they exist
    cols_to_keep = [c for c in [
        "id", "name", "locality", "country.name",
        "coordinates.latitude", "coordinates.longitude"
    ] if c in df.columns]

    return df[cols_to_keep]