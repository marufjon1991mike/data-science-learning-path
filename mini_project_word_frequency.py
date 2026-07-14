#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 18:09:34 2026

@author: khalievmarufjon
"""

# Foydalanuvchidan uzun bir matn (bir necha jumla) kiritishini so'rang. Dastur:

# Matnni so'zlarga ajratsin (.split())
# Har bir so'z necha marta takrorlanganini dictionary'da hisoblasin
# Eng ko'p takrorlangan 3 ta so'zni chiqarib bersin

matn =""" Python dasturlash tili juda qiziqarli. Python bilan siz ma'lumotlarni tahlil qilishingiz 
    mumkin. Ma'lumotlar bilan ishlash uchun Python eng yaxshi til hisoblanadi. Data science 
    sohasida Python juda mashhur. Men Python o'rganishni davom ettirmoqchiman."""

matn = matn.lower() # matn ichidagi har bir so'zni kichik harflarga o'tkazadi

matn = matn.replace(".", "") # tinish belgilarni olib tashlash uchun
matn = matn.replace(",", "")
matn = matn.replace("!", "")
matn = matn.replace("?", "")

sozlar = matn.split() # matndagi har bir so'zni alohida ajratadi

sozlar_soni = {} # bu lug'atda har bir so'z necha marta takrorlanganini saqlaydi

for soz in sozlar:
    if soz in sozlar_soni:
        sozlar_soni[soz] += 1
    else:
        sozlar_soni[soz] = 1

sozlar_soni_nusxa = sozlar_soni.copy() # asosiy lug'atni yo'qotmaslik uchun uni nusxalaymiz

for i in range(1, 4):
    eng_kop_soz = None
    eng_katta_son = 0
    for soz, son in sozlar_soni_nusxa.items():
        if son > eng_katta_son:
            eng_katta_son = son
            eng_kop_soz = soz
    print(f"{i}. {eng_kop_soz} - {eng_katta_son} marta")
    sozlar_soni_nusxa[eng_kop_soz] = 0
 







