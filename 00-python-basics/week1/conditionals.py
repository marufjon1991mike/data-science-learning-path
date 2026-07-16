#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 12:49:56 2026

@author: khalievmarufjon
"""
# 12.07.2026

# task_1
# Foydalanuvchidan yoshini so'rang: agar 18 dan katta bo'lsa "Kattasiz", aks holda "Voyaga yetmagansiz" deb chiqaring

yosh = int(input("Yoshingizni kiriting: "))
if yosh > 18:
    print("Siz 18 yoshdan kattasiz")
else:
    print("Siz voyaga yetmagansiz")
    
# task_2
# Uchta sonni kiritib, ular orasidan eng kattasini toping (if/elif/else bilan)

son_1 = int(input("1-Sonni kiriting: "))
son_2 = int(input("2-Sonni kiriting: "))
son_3 = int(input("3-Sonni kiriting: "))
if son_1 >= son_2 and son_1 >= son_3:
    print(f"{son_1}, {son_2} va {son_3} sonlar orasida eng kattasi {son_1}")
elif son_2 >= son_1 and son_2 >= son_3:
    print(f"{son_1}, {son_2} va {son_3} sonlar orasida eng kattasi {son_2}")
else:
    print(f"{son_1}, {son_2} va {son_3} sonlar orasida eng kattasi {son_3}")

#task_3
# Foydalanuvchidan baholarini so'rang (0-100) va harf bahosini chiqaring (90+ = A, 80-89 = B, va h.k.)

baho = int(input("Bahoyingizni kiriting: "))
if baho >= 90:
    harf = "A"
elif baho >=80:
    harf = "B"
elif baho >= 70:
    harf = "C"
elif baho >= 60:
    harf = "D"
else:
    harf = "F"
print(f"Sizning natijangiz {baho} = {harf}")
    
    
# task 4
# Ikki xonali son kiritib, u juft yoki toq ekanligini, shuningdek musbat yoki manfiy ekanligini aniqlang

son = int(input("Ikki xonali sonni kiriting: "))
if son % 2 == 0 and son > 0:
    print(f"Siz kiritgan {son} soni juft va musbat son")
elif son % 2 == 0 and son < 0:
    print(f"Siz kiritgan {son} soni juft va manfiy son")
elif son % 2 != 0 and son > 0:
    print(f"Siz kiritgan {son} soni toq va musbat son")
else:
    print(f"Siz kiritgan {son} soni toq va manfiy son")


