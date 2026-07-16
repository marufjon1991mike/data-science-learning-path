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
    print("1. Yangi xarajatlar qo'shish")
    print("2. Barcha xarajatlarni ko'rish")
    print("3. Jami xarajatlarni hisoblash")
    print("4. Chiqish")

# Xarajat qo'shish funksiyasi

# Funksiya yozing — nomi va summasini so'rasin, try/except bilan summa xato kiritilishini tekshirsin, 
# so'ng faylga "a" rejimida yozsin (masalan, "non,5000\n" formatida).

def jami_hisobla():
    jami = []
    try:
        with open("xarajatlar.txt", "r") as fayl:
            for qator in fayl:
                nomi, summa = qator.strip().split(",")
                summa = int(summa)
                jami.append(summa)
            print(f"Jami xarajatlar {sum(jami)} so'm bo'ldi.")
    except FileNotFoundError:
        print("Hozircha xarajat yo'q!")

        
def xarajatlarni_korsat():
    try:
        with open("xarajatlar.txt", "r") as fayl:
            for qator in fayl:
                nomi, summa = qator.strip().split(",") # qator.strip() — qator oxiridagi \n belgisini olib tashlaydi
                                                    # .split(",") — vergul bo'yicha ikkiga ajratadi: ["kartoshka", "20000"]
                print(f"{nomi} : {summa} so'm")
    except FileNotFoundError:
        print("Hozircha xarajat yo'q!")
    
def xarajat_qoshish():
    nomi = input("Xarajat nomini kiriting: ")
    try:
        summa = int(input("Summani kiriting: "))
        with open("xarajatlar.txt", "a") as fayl:
            fayl.write(f"{nomi},{summa}\n")
        print("Xarajat qo'shildi!")
    except ValueError:
        print("Iltimos xarajatlarni son bilan kiriting!")
        
while True:
    menyu()
    tanlov = input("Tanlovingizni kiriting: ")
    if tanlov == "4":
        print("Dastur yopildi")
        break
    elif tanlov == "1":
        xarajat_qoshish()
    elif tanlov == "2":
        xarajatlarni_korsat()
    elif tanlov == "3":
        jami_hisobla()




            
    

    



