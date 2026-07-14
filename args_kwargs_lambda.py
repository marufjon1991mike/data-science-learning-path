#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 20:56:51 2026

@author: khalievmarufjon
"""

# 14.07.2026

# task_1
# *args yordamida, istalgan miqdordagi sonlarni qabul qilib, ularning eng kattasini topadigan 
# funksiya yozing (max() funksiyasisiz, if bilan)

def eng_katta_son(*sonlar):
    eng_katta = sonlar[0]
    for son in sonlar:
        if eng_katta < son:
            eng_katta = son
    return eng_katta
natija = eng_katta_son(12, 15, 4, 18, 13)
print(natija)

# task_2 
# lambda yordamida, bitta sonni qabul qilib, uni 3 ga ko'paytiradigan funksiya yozing

kopaytma = lambda x: x * 3
print(kopaytma(5))

# task_3
# Shuni yozib ko'ring: **kwargs yordamida, foydalanuvchi bergan barcha mahsulot va narxlarni qabul 
# qilib, ularning jami summasini hisoblaydigan funksiya:
    
def jami_hisobla(**mahsulotlar):
    

    
print(jami_hisobla(non=5000, sut=8000, tuxum=15000))