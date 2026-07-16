#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 18:03:12 2026

@author: khalievmarufjon
"""
# 13.07.2026

# task_1
# Listdagi takrorlanuvchi elementlarni olib tashlab, faqat noyob (unique) qiymatlarni qoldiring 
# (list orqali, set() ishlatmasdan)
shaharlar = ["Sirdaryo", "Samarqand", "Jizzax", "Toshkent", "Navoiy", "Samarqand", "Jizzax"]
yangi_royxat = []
for shahar in shaharlar:
    if shahar not in yangi_royxat:
        yangi_royxat.append(shahar)
print(yangi_royxat)

# task_2
# Foydalanuvchidan 5 ta son ketma-ket kiritilishini so'rang, ularni listga saqlang va o'rtachasini hisoblang
sonlar = []
print("5 ta son kiriting!")

for i in range(1, 6):
    user = int(input(f"{i}-sonni kiriting: "))
    sonlar.append(user)

mean = sum(sonlar) / len(sonlar)
print(mean)
    
   
# task_3
# Ikkita listni birlashtirib (+ yoki extend()), natijani saralab (sort()) chiqaring
quruq_meva = ["bodom", "mayiz", "pista"]
hol_meva = ["uzum", "shaftoli", "olma"]
mevalar = []
mevalar.extend(quruq_meva)
mevalar.extend(hol_meva)
mevalar.sort()
print(mevalar)

# task_4
# O'z ma'lumotlaringizni dictionary sifatida saqlang: {"ism": "Kamol", "yosh": 25, "shahar": "Navoiy"}, 
# so'ng har bir kalit-qiymatni alohida chop eting (.items() bilan)
info = {"ism": "Kamol", "yosh": 25, "shahar": "Navoiy"}
for key, value in info.items():
    print(f"{key} : {value}")

# task_5
# Talabalar va ularning baholarini saqlovchi dictionary yarating (masalan, {"Ali": 85, "Vali": 92, "Sami": 78}), 
# so'ng eng yuqori bahoga ega talabani toping
talabalar = {
    "Ali": 85, 
    "Vali": 92, 
    "Sami": 78
    }
max_baho = max(talabalar.values())
for key, value in talabalar.items():
    if value == max_baho:
        print(f"Eng yuqori baho olgan talaba {key}")
    
# task_6
# Foydalanuvchidan mahsulot nomi va narxini ketma-ket kiritishni so'rang (5 marta), ularni 
# dictionary'ga saqlang, so'ng jami summani hisoblang

mahsulotlar = {}
for i in range(1, 6):
    nomi = input(f"{i}-mahsulot nomini kiriting: ")
    narxi = int(input(f"{i}-mahsulot narxini kiriting: "))
    mahsulotlar[nomi] = narxi
for key, value in mahsulotlar.items():
    print(f"{key} {value} so'm.")
jami = sum(mahsulotlar.values())
print(f"Mahsulotlarning jami narxi {jami} so'm")
        
# task_7
# Ikkita set yarating (masalan, {1,2,3,4,5} va {4,5,6,7,8}), ularning kesishmasi (intersection), 
# birlashmasi (union) va farqini (difference) toping
A = {1,2,3,4,5}
B = {4,5,6,7,8}
kesishma = A.intersection(B)
birlashma = A.union(B)
farq = A.difference(B)
print(kesishma)
print(birlashma)
print(farq)

# task_8
# Berilgan matndagi noyob so'zlarni set yordamida aniqlang (masalan, "salom dunyo salom python" dan takrorlanmagan so'zlar ro'yxatini chiqaring)
matn = "salom dunyo salom python"
ajratish = matn.split()
uniqe_sozlar = set(ajratish)
print(uniqe_sozlar)















