#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 21:42:25 2026

@author: khalievmarufjon
"""

# 16.07.2026

import numpy as np

# task_1 [10, 20, 30, 40, 50] ro'yxatidan NumPy array yarating, chop eting, type() bilan turini tekshiring.

arr = np.array([10, 20, 30, 40, 50])
print(type(arr))

# task_2 np.arange(1, 11) bilan 1 dan 10 gacha array yarating.

arr_2 = np.arange(1, 11)

# task_3 Yuqoridagi array'dan [3:7] slicing bilan qism oling.

arr_slice = arr_2[3:7]

# task_4 np.zeros(5) va np.ones(5) ni sinab ko'ring, natijalarini chop eting.

arr_3 = np.zeros(5)
print(arr_3)

arr_4 = np.ones(5)
print(arr_4)

# task_5 2 o'lchamli array yarating (np.array([[1, 2, 3], [4, 5, 6]])), .shape xususiyatini tekshiring.
arr_5 = np.array(([1, 2, 3],[4, 5, 6]))
print(arr_5.shape)

arr_6 = np.array([[1,2],[3,4],[5,6]])
print(arr_6.shape)