#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 15:15:06 2026

@author: khalievmarufjon
"""

# 15.07.2026

# task_1
# 5 ta shahar nomini o'z ichiga olgan shaharlar.txt faylini yarating (write bilan, har birini yangi 
# qatorga yozing — \n dan foydalaning):
with open("shaharlar.txt", "w") as fayl:
    fayl.write("Toshkent\n")
    fayl.write("Samarqand\n")
    fayl.write("Namangan\n")
    fayl.write("Xorazm\n")
    fayl.write("Andijon\n")

# task_2
# Yuqorida yaratgan faylni o'qib, har bir shahar nomini alohida qatorda chop eting:

with open("shaharlar.txt", "r") as fayl:
    for shahar in fayl:
        print(shahar)
        print(shahar.strip()) # har bir qatordan \n ni olib tashlaydi

# task_3
# Faylga yangi shahar qo'shing, lekin eski ma'lumotni o'chirmasdan (bunda "w" emas, "a" — append — rejimi kerak bo'ladi):

with open("shaharlar.txt", "a") as fayl:
    fayl.write("Buxoro\n")