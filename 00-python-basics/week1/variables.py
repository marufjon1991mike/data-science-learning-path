#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 11:47:05 2026

@author: khalievmarufjon
"""
# 12.07.20026 python-data-science-journey
# task_1
# Ismingiz, yoshingiz va shahringizni o'zgaruvchilarga saqlang, so'ng ularni bitta jumla qilib chop eting 
# (masalan: "Mening ismim Ali, men 25 yoshdaman, Toshkentda yashayman")

ism = "Kamol"
yosh = 25
shahar = "Navoiy"
natija = f"Mening ismim {ism}, men {yosh} yoshdaman, {shahar}da yashayman."
print(natija)

# task_2
# Ikkita son kiritib (input orqali), ularning yig'indisi, ayirmasi, ko'paytmasi va bo'linmasini hisoblang
 
son_1 = int(input("Birinchi sonni kiriting: "))
son_2 = int(input("Ikkinchi sonni kiriting: "))

if son_2 == 0:
    print("Har qanday sonni 0 ga bo'lib bo'lmaydi.")
else:
    yigindi = son_1 + son_2
    ayirma = son_1 - son_2
    kopaytma = son_1 * son_2
    bolinma = son_1 / son_2
    print(f"{son_1} va {son_2} ning yig'indisi {yigindi}, ayirmasi {ayirma}, ko'paytmasi {kopaytma} va bo'linmasi {bolinma} ga teng")

# task_3
#Foydalanuvchidan uning ish haqini kiritishini so'rang va yillik daromadini hisoblab chiqing (oylik × 12)

oylik_maosh_som = int(input("Oylik ish haqingiz qancha? "))
yillik = oylik_maosh_som * 12
print(f"Sizning yillik maoshingiz {yillik} so'm")

# task_4
#Ikkita sonni kiritib, ular teng yoki yo'qligini == operatori bilan tekshiring va natijani chop eting
son_a = int(input("Birinchi sonni kiriting: "))
son_b = int(input("Ikkinchi sonni kiriting: "))
if son_a == son_b:
    print(f"{son_a} va {son_b} teng sonlar")
else:
    print(f"{son_a} va {son_b} sonlar teng emas")

# task_5
#Temperaturani Selsiydan Farengeytga o'giruvchi dastur yozing (formula: F = C × 9/5 + 32)

temp = int(input("Temperaturani kiriting: "))
faren = temp * 9 / 5 + 32
print(f"Temperatura {temp} - Farengeyt {faren}")


