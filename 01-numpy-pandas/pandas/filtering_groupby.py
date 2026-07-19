#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 14:22:47 2026

@author: khalievmarufjon
"""
# 19.07.2026

import pandas as pd

malumot = {
    "ism" : ["Ali", "Vali", "Kamol", "Jamol"],
    "yosh" : [29, 18, 17, 19],
    "shahar" : ["Navoiy", "Jizzax", "Buxoro", "Toshkent"]
    }
df = pd.DataFrame(malumot)

# task_1 DataFrame'dan faqat 18 yoshdan katta bo'lganlarni filtrlab chop eting.

print(df[df["yosh"]>18])

# task_2 DataFrame'ga yangi ustun qo'shing — "maosh" (har biriga o'zingiz xohlagan sonlar bering), 
# so'ng faqat maoshi 5000 dan yuqori bo'lganlarni filtrlang.

df["maosh"] = [3000, 5000, 7000, 10000]

print(df[df["maosh"]>5000])

# task_3 Kengaytirilgan dataset yarating (kamida 6 ta odam, ba'zilari bir xil shaharda),
# so'ng groupby("shahar") yordamida har bir shahar bo'yicha o'rtacha yoshni hisoblang.

malumot_2 = {
    "ism" : ["Ali", "Vali", "Kamol", "Jamol", "Jasur", "Tohir"],
    "yosh" : [29, 18, 17, 19, 35, 23],
    "shahar" : ["Navoiy", "Jizzax", "Buxoro", "Toshkent", "Jizzax", "Navoiy"]
    }
df2 = pd.DataFrame(malumot_2)

print(df2.groupby("shahar")["yosh"].mean())