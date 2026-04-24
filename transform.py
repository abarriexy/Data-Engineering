# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 20:51:31 2026

@author: Amadu
"""

import pandas as pd

def to_dataframe(results):
    if not results:
        return pd.DataFrame()

    return pd.json_normalize(results)


def clean_data(df):
    if df.empty:
        return df

    df["date.utc"] = pd.to_datetime(df["date.utc"])

    columns = ["location", "parameter", "value", "unit", "date.utc"]
    return df[columns]