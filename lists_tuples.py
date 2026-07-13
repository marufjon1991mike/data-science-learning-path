#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 16:53:52 2026

@author: khalievmarufjon
"""

# 13.07.2026

# task_1
# Bo'sh list yarating, unga append() orqali 5 ta mevaning nomini qo'shing, so'ng listni chop eting
mevalar = []
mevalar.append("olma")
mevalar.append("anor")
mevalar.append("shaftoli")
mevalar.append("uzum")
mevalar.append("anjir")
print(mevalar)

# task_2
# Berilgan list [12, 45, 3, 67, 21, 9] dan eng katta va eng kichik sonni topib chiqaring (max() 
# va min() funksiyalarisiz, faqat sikl bilan)
sonlar = [12, 45, 3, 67, 21, 9]
eng_katta = sonlar[0]
eng_kichik = sonlar[0]
for son in sonlar:
    if eng_katta < son:
        eng_katta = son
for son in sonlar:
    if eng_kichik > son:
        eng_kichik = son
print(f"Ro'yxat ichidagi sonlar orasidan eng kattasi {eng_katta}.")
print(f"Ro'yxat ichidagi sonlar orasidan eng kichigi {eng_kichik}.")
    
# task_3
# List ichidagi barcha juft sonlarni yangi listga ajratib oling (masalan, [1,2,3,4,5,6] dan [2,4,6] ni chiqaring)

sonlar = [12, 45, 24, 3, 67, 46, 21, 9, 18]
juft_sonlar = []
for son in sonlar:
    if son % 2 == 0:
        juft_sonlar.append(son) 
print(juft_sonlar)
        
# task_4
# Listni teskari tartibga aylantiring (reverse() metodisiz, faqat slicing — [::-1] — yordamida)

sonlar = [12, 45, 24, 3, 67, 46, 21, 9, 18]
teskari_tartib = sonlar[::-1]
print(teskari_tartib)

# task_5
# Ism va yoshni tuple sifatida saqlang (masalan, ("Kamol", 25)), so'ng tuple ichidagi qiymatlarni 
# alohida o'zgaruvchilarga ajrating (unpacking)

info = ("Kamol", 25)
ism, yosh = info # unpacking usuli
print(ism)
print(yosh)

 

