#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 16:42:14 2026

@author: khalievmarufjon
"""

# 14.07.2026
# task_1 
# Ikkita sonni parametr sifatida qabul qilib, yig'indisini return orqali qaytaradigan funksiya:

def yigindi_hisobla(son_1, son_2):
    natija = son_1 + son_2
    return natija
    
print(yigindi_hisobla(15, 10))

# task_2
# Bitta sonni oladigan va uning juft/toqligini return orqali qaytaradigan funksiya:
def juft_yoki_toq(son):
    if son % 2 == 0:
        natija = f"{son} juft son"
    else:
        natija = f"{son} toq son"
    return natija
print(juft_yoki_toq(13))
print(juft_yoki_toq(16))

# task_3
# Standart qiymatli parametr bilan salomlashish funksiyasi:
 
def salomlashish(ism="Mehmon"):
    natija = f"Salom {ism}"
    return natija
print(salomlashish())
print(salomlashish("Ali"))
    
    