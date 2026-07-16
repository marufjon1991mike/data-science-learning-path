#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 22:10:04 2026

@author: khalievmarufjon
"""

# 16.07.2026

import numpy as np

# task_1 [5, 10, 15, 20, 25] array yarating, har bir elementga 3 qo'shib, natijani chop eting.

arr = np.array([5, 10, 15, 20, 25])
arr = arr + 3
print(arr)

# task_2 Yuqoridagi array'ning har bir elementini 2 ga bo'lib, natijani chop eting.

arr_2 = arr / 2
print(arr_2)

# task_3 np.array([10, 20, 30, 40, 50]) array uchun quyidagi statistik funksiyalarni sinab ko'ring va natijalarni chop eting:

arr_3 = np.array([10, 20, 30, 40, 50]) 
print(arr_3.mean())   # o'rtacha
print(arr_3.sum())    # yig'indi
print(arr_3.max())    # eng katta
print(arr_3.min())    # eng kichik
print(arr_3.std())    # standart chetlanish

# task_4 Ikkita array yarating (a = np.array([1,2,3]), b = np.array([10,20,30])), ularni bir-biriga qo'shing (a + b) — natija nima bo'lishini oldindan bashorat qiling, keyin sinab tekshiring.

a = np.array([1,2,3])
b = np.array([10,20,30])
print(a + b)
