import numpy as np
import sys
import array
import random
import matplotlib.pyplot as plt

# rng = np.random.default_rng(1)
# s = rng.random(50)
# print(s)
# print(sum(s))
# print(np.sum(s)) # быстрее для больших и особенно многомерных массивов
# --------------------
# a = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])
# print(np.sum(a))
# print(np.sum(a, axis = 1)) # получаем массив
# print(np.sum(a, axis = 0))
#
# print(np.min(a))
# print(np.min(a, axis = 0))
# print(np.min(a, axis = 1))
#
# print(np.nanmin(a)) #безопасно для NaN
# print(np.nanmin(a, axis = 0))
# print(np.nanmin(a, axis = 1))

# --------------------------
# #Транстирование (broadcasting)
#
# a = np.array([0, 1, 2])
# b = np.array([5, 5, 5])
#
# print(a + b)
# print(a + 5) # 5 broadcast in [5, 5, 5]
#
# a = np.array([[0, 1, 2], [3, 4, 5]])
# print(a + 5)
#
# a = np.array([0, 1, 2])
# b = np.array([[0], [1], [2]])
# print(a + b)
# [[0 1 2]
#  [1 2 3]
#  [2 3 4]]

# 1 если размерности отличаются, форма с меньшей дополняется на 1 с лева
# a = np.array([[0, 1, 2], [3, 4, 5]])
# b = np.array([5])
# print(a.shape, b.shape)
# print(a + b) #


# 2 если формы не совпадают, то если у массива форма равна 1, то он
# растягивается

# 3 если после этих правил размеры отличаются - ошибка

# a = np.ones((2, 3))
# b = np.arange(3)
# print(a)
# print(b)
#
# print(a.shape, b.shape)
#
# #(2, 3)  (2, 3)
# # (3,) -> (1, 3) -> (2, 3)
# c = a + b
# print(c)
#
##########

# a = np.arange(3).reshape((3,1))
# b = np.arange(3)
#
# print(a)
# print(b)
#
# #(3, 1) -> (3, 3)
# #(3, ) -> (1, 3) -> (3, 3)
#
# print(a + b)

#######

# a = np.ones((3, 2))
# b = np.arange(3)

# dim =2  shape = (3, 2)
# dim = 1 shape = (3, )

# 2 (3, 2) (3, 2)
# 1 (3, ) -> (1, 3) -> (3, 3) - размеры отличаются - ошибка

# -------------------------
# центрирование
# x = np.array([
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [9, 8, 7, 6, 5, 4, 3, 2, 1]
# ])
#
# xmean = x.mean(0) #0 - нулевое измерение (по строкам)
# print(xmean)
#
# xcenter = x - xmean
# print(xcenter) #центрирование 0
#
# xmean1 = x.mean(1)
# print(xmean1)
# xmean1 = xmean1[:,  np.newaxis]
# print(xmean1)
# xcenter1 = x - xmean1
# print(xcenter1)
# -------------------------
# x = np.linspace(0, 5, 50)
# y = np.linspace(0, 5, 50)[:, np.newaxis]
# z = np.sin(x)**3 + np.cos(20 + y*x)*np.sin(y)
# print(z.shape)
# plt.imshow(z)
# plt.colorbar()
# plt.show()
# -------------------

# x = np.array([1, 2, 3, 4, 5])
# y = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(x < 3)
# print(np.less(x, 3))
#
# print(np.sum(y < 4))
# print(np.sum(y < 4, axis = 0)) #по столбцам
# print(np.sum(y < 4, axis = 1)) #по строкам

# & | ^ ~

# Q2 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# x = np.array([1, 2, 3, 4, 5])
# print(x < 3)
# print(x[x < 3])
# print(bin(42))
# print(bin(59))
# print(bin(42 & 59))


# -----------------------

# Векторизация индекса

# x = np.array([1, 2, 3, 4, 5, 6,7, 8, 9])
# index = [1, 5, 7]
#
# print(x[index])
#
# index = [[1, 5, 7], [2, 4, 8]]
# print(x[index])

# результат - как в index

# x = np.arange(12).reshape(3,4)
#
# print(x)
# print("---")
# print(x[2, [2, 0, 1]])
# print("---")
# print(x[1:, [2, 0, 1]])
# первый срез - за первую размерность, второй срез - уровнь ниже

# x = np.arange(10)
# i = np.array([2, 1, 8, 4])
# x[i] = 999

# SORT
#
# x = [3, 4, 6, 43, 7, 23, 8, 2, 3, 4]
# print(sorted(x))
# print(np.sort(x)) #умеет по размерностям и быстрее на больхих данных
# print(x.sort())

# структурированные массивы
# data = np.zeros(4, dtype = {
#     'names' : [ # аргумент
#         'name', 'age'
#     ],
#     'formats': [ # аргумент
#         'U10', 'i4' ## utf - char s; int
#     ]
# })
#
# print(data.dtype)
#
# name = ['name1', 'name2', 'name3', 'name4']
# age = [10, 20, 30, 40]
#
# data['name'] = name
# data['age'] = age
#
# print(data)
# print(data['age'] > 20)
#
# #------------------------------------
#
# #Массивы записей
#
# data_rec = data.view(np.recarray)
# print(data_rec)
# print(data_rec[0])  #можно по индексам
# print(data_rec[-1].name)
