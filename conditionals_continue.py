#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 15:39:54 2026

@author: khalievmarufjon
"""
# 12.07.2026

# task_1

# 1-usul
# 1 dan 100 gacha bo'lgan barcha juft sonlarning yig'indisini hisoblang (for sikli bilan)

# juft_sonlar = []
# for i in range(101):
#     if i > 0 and i % 2 == 0:
#         juft_sonlar.append(i)
    
# print("1 dan 100 gacha bo'lgan juft sonlar yig'indisi", sum(juft_sonlar), "ga teng")

# 2-usul
# jami = 0
# for i in range(1,101):
#     if i % 2 == 0:
#         jami += i
# print(f"1 dan 100 gacha bo'lgan juft sonlar yig'indisi {jami} ga teng")
    
# 3-usul
# jami = 0
# for i in range(2,101,2):
#     jami += i
# print(f"1 dan 100 gacha bo'lgan juft sonlar yig'indisi {jami} ga teng")


# task_2
# Foydalanuvchi "stop" deb yozguncha sonlarni kiritishni so'rang va oxirida ularning o'rtachasini 
# chiqaring (while sikli bilan)

# i = 1
# sonlar = []
# while True:
#     son = input(f"{i}-sonni kiriting: ")
#     if son.lower() == "stop":
#         break
#     son = int(son)
#     sonlar.append(son)
#     i += 1
# if len(sonlar) > 0:
#     print(f"Sonlarning o'rtacha qiymati {sum(sonlar) / len(sonlar)}")
# else:
#     print("Siz hech qanday son kiritmadingiz!")

# task_3
# Berilgan sonning faktorialini hisoblang (masalan, 5! = 5×4×3×2×1)

# son = int(input("Son kiriting: "))

# if son < 0:
#     print("Manfiy sonla uchun faktorial aniqlanmagan")
# else:
#     faktorial = 1
#     for i in range(1, son + 1):
#         faktorial *= i 
#     print(f"{son} ning faktoriali {faktorial} ga teng")

# task_4
# 1 dan 50 gacha bo'lgan barcha tub sonlarni (prime numbers) topib chop eting



# "Kotirovka jadvali" — foydalanuvchi kiritgan sonning 1 dan 10 gacha ko'paytma jadvalini chiqaring (masalan, 5 kiritilsa: 5x1=5, 5x2=10, ...)
 



































