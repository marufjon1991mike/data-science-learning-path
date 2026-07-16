#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 22:28:59 2026

@author: khalievmarufjon
"""

# 16.07.2026

import pandas as pd

# task_1
# Yuqoridagi kabi, 4 ta do'stingiz (ism, yosh, shahar) haqida dictionary yarating, undan DataFrame hosil qiling va chop eting.

malumot = {
    "ism" : ["Ali", "Vali", "Kamol", "Jamol"],
    "yosh" : [29, 18, 17, 19],
    "shahar" : ["Navoiy", "Jizzax", "Buxoro", "Toshkent"]
    }
df = pd.DataFrame(malumot)
print(df)

# task_2 DataFrame'ning quyidagi xususiyatlarini sinab ko'ring:

print(df.shape)      # (qatorlar, ustunlar) soni
print(df.columns)    # ustun nomlari
print(df.dtypes)     # har bir ustunning ma'lumot turi
print(df.info())     # umumiy ma'lumot    

# task_3 Faqat bitta ustunni tanlab chop eting:

print(df["ism"])

# task_4 Faqat yosh ustunidagi qiymatlarning o'rtachasini toping (.mean()).

print(df["yosh"].mean())

# task_5 DataFrame'ning birinchi 2 ta qatorini ko'rsating (.head(2)).
print(df.head(2))













