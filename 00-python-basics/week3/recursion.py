#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 04:52:22 2026

@author: khalievmarufjon
"""

# 15.07.2026

#Faktorialni rekursiya bilan yozib, sinab ko'ring
def faktorial(son):
    if son == 0 or son == 1: # Bazaviy holat (base case) — qachon to'xtash kerakligini aytadi (aks holda funksiya cheksiz o'zini chaqiraverib, xato beradi)
        return 1
    else:
        return son * faktorial(son - 1)  # rekursiv chaqiruv
print(faktorial(5))

# task_2
# Berilgan sondan 1 gacha bo'lgan barcha sonlarning yig'indisini rekursiya bilan hisoblang
# (masalan, yigindi(5) = 5+4+3+2+1 = 15):
 
def yigindi(son):
    if son == 0:
        return 0
    else:
        return son + yigindi(son - 1)
print(yigindi(5))
print(yigindi(0))
print(yigindi(1))