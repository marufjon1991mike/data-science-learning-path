#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 16:44:19 2026

@author: khalievmarufjon
"""
# 15.07.2026

# loyiha
# Konsol dasturi yarating, u quyidagilarni bajarishi kerak:

# Menyu ko'rsatish — foydalanuvchiga tanlov beradi:

#    1. Yangi xarajat qo'shish
#    2. Barcha xarajatlarni ko'rish
#    3. Jami xarajatni hisoblash
#    4. Chiqish

# Xarajatlarni faylga saqlash — har bir xarajat (nomi, summasi) xarajatlar.txt fayliga yoziladi, 
# dastur yopilib qayta ochilganda ham ma'lumot yo'qolmasligi kerak
# Xatolarni boshqarish — agar foydalanuvchi summa o'rniga harf kiritsa, dastur qulamasligi kerak

def menyu():
    print("1. Yangi xarajatlaar qo'shish")
    print("2. Barcha xarajatlaarni ko'rish")
    print("3. Jami xarajatlarni hisoblash")
    print("4. Chiqish")

while True:
    menyu()
    tanlov = input("Tanlovingizni kiriting: ")
    if tanlov == "4":
        print("Dastur yopildi")
        break

