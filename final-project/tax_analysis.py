#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 15:01:37 2026

@author: khalievmarufjon
"""

# 19.07.2026

import pandas as pd
df = pd.read_csv("final_data_2023.csv")
print(df.head())
print(df.info())
print(df.shape)
df.head()