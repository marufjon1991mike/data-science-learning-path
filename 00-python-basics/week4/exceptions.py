#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 15:38:08 2026

@author: khalievmarufjon
"""

# 15.07.2026

# task_1
# Foydalanuvchidan son so'rang. Agar u son o'rniga harf kiritsa, dastur qulamasdan, 
# "Iltimos, faqat son kiriting" deb chiqarsin (ValueError ni ushlang).

try:
    son = int(input("Son kiriting: "))
    print(f"Siz {son} sonini kiritdingiz")
except ValueError:
    print("Iltimos son kiriting!")

# task_2
# Ikkita son so'rab, birinchisini ikkinchisiga bo'ling. Agar ikkinchi son 0 bo'lsa, 
# ZeroDivisionError ni ushlab, tegishli xabar chiqaring.
try: 
    son_1 = int(input("1-sonni kiriting: "))
    son_2 = int(input("2-sonni kiriting: "))
    natija = son_1 / son_2
    print(natija)
except ZeroDivisionError:
    print("Sonni 0 ga bo'lib bo'lmaydi")
except ValueError:
    print("Iltimos faqat son kiriting!")

# task_3
# Mavjud bo'lmagan faylni ochishga urinib ko'ring (masalan, "yoq_fayl.txt"), va FileNotFoundError 
# ni ushlab, "Fayl topilmadi" deb chiqaring.

try:
    with open("yoq_fayl.txt", "r") as fayl:
        natija = fayl.read()
        print(natija)
except FileNotFoundError:
    print("Fayl topilmadi")