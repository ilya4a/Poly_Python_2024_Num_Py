import numpy as np
import sys
import array
import random
import pandas as pd

# pandas - строки и столбцы индексируются метками, а не только числовыми значениями
# series, DataFrame, Index

# Series
# data = pd.Series([0.25, 0.5, 0.75, 1.0])
# print(data, type(data))
# print(type(data.values), type(data.index))
#
# print(data[0])
# print(data[1:3])
# print(data[1:3])


# data = pd.Series([0.25, 0.5, 0.75, 1.0], index = ['a', 'b', 'c', 'd'])
# print(data)
# print(data['a'])
# print(data['b':'d'])
#
#
# data = pd.Series([0.25, 0.5, 0.75, 1.0], index = [1, 7, 'c', 'd'])
# print(data)
# print(data[7:'c'])

# population_dict = {
#     'city_1' : 1001,
#     'city_2' : 1002,
#     'city_3' : 1003,
#     'city_4' : 1004,
#     'city_5' : 1005,
# }
#
# population = pd.Series(population_dict)
#
# print(population)
# для создания Series
# списки Python или NumPy
# скалярные значения

# 1----------------------------------------------

# DataFrame - двумерный массив с явно опред индексами
# - последовательность согласованных по индексам обьектов Series
# population_dict = {
#     'city_1' : 1001,
#     'city_2' : 1002,
#     'city_3' : 1003,
#     'city_4' : 1004,
#     'city_5' : 1005,
# }
#
# area_dict = {
#     'city_1' : 9001,
#     'city_2' : 9002,
#     'city_3' : 9003,
#     'city_4' : 9004,
#     'city_5' : 9005,
# }
#
# population = pd.Series(population_dict)
# area = pd.Series(area_dict)
#
# states = pd.DataFrame({
#     'population' : population,
#     'area': area,
# })
# print(states)
#
# print(states.values)
# print(states.columns)
# print(states.index)
#
# print(type(states.values))
# print(type(states.columns))
# print(type(states.index))
#
# print(states['area'])


# способы создания
# через series
# списки словарей
# словари обьектов series
# двумерный массив numpy
# структурированный массив numpy

# 2-----------------------------------------

# Index - способ организации ссылки на данные Series and DataFrame

# Index - следует соглашениям set

# indA = pd.Index([1, 2, 3, 4, 5])
# indB = pd.Index([2, 3, 4, 5, 6])
#
# print(indA.intersection(indB))

# Выборка данных

# data = pd.Series([0.25, 0.5, 0.75, 1.0])
# data = pd.Series([0.25, 0.5, 0.75, 1.0], index = ['a', 'b', 'c', 'd'])
#
# print('a' in data)
# print('x' in data)
#
# print(data.keys())
# print(list(data.items()))
# data['a'] = 100
# print(data)
# data['z'] = 99
# print(data)

# как одномерный массив
# data = pd.Series([0.25, 0.5, 0.75, 1.0], index = ['a', 'b', 'c', 'd'])
# print(data['a': 'c']) #обе включительно!!!
# print(data[0:2])
# print(data[(data > 0.5) & (data < 1)])
# print(data[['a', 'd']]) #векторизованная индексация
#
#
# # атрибуты индексаторы
# data = pd.Series([0.25, 0.5, 0.75, 1.0], index = [1, 3, 10, 14])
# print(data[1]) # первый элемент, а не второй!!!!
#
# print(data.loc[1]) # просто индекс
# print(data.iloc[1]) # номер в индексе

# -----------------------------------------

# p =pd.Series({
#     'city_1' : 1001,
#     'city_2' : 1002,
#     'city_3' : 1003,
#     'city_4' : 1004,
#     'city_5' : 1005,
# })
# a = pd.Series({
#     'city_1' : 9001,
#     'city_2' : 9002,
#     'city_3' : 9003,
#     'city_4' : 9004,
#     'city_5' : 9005,
# })

# как словарь
# data = pd.DataFrame({'area' : a, 'population' : p, 'pop': p})
#
# print(data['area'])
# print(data.area)
#
# print("------------")
#
# print(data.pop is data['pop']) #False - одинаковые значения у pop and population
# print(data.area is data['area']) #True
#
# data['new'] = data['area']
#
# data['new'] = data['area'] / data['population']
#
# print(data)

# --------------------------

# как двумерный массив numpy

# p =pd.Series({
#     'city_1' : 1001,
#     'city_2' : 1002,
#     'city_3' : 1003,
#     'city_4' : 1004,
#     'city_5' : 1005,
# })
# a = pd.Series({
#     'city_1' : 9001,
#     'city_2' : 9002,
#     'city_3' : 9003,
#     'city_4' : 9004,
#     'city_5' : 9005,
# })

# data = pd.DataFrame({'area' : a, 'population' : p, 'pop': p})

# print(data)
# print(data.values)
# print(data.T) #transpon
# print(data['area'])
# print(data.values[0])
# print(data.values[0:3])

# атрибуты индексаторы
# print(data)
#
# print(data.iloc[:3, 1:2]) #индексы, потом колонки
# print(data.loc[:'city_3', 'population':'pop'])
# print(data.loc[data['pop'] > 1002, ['area', 'pop']] )
#
# data.iloc[0, 2] = 99999
# print(data)

# -------------------------------------------


# rnd = np.random.default_rng()
# s = pd.Series(rnd.integers(0, 10, 4))
#
# print(s)
# print(np.exp(s))
# p =pd.Series({
#     'city_1' : 1001,
#     'city_2' : 1002,
#     'city_3' : 1003,
#     'city_41' : 1004,
#     'city_51' : 1005,
# })
# a = pd.Series({
#     'city_1' : 9001,
#     'city_2' : 9002,
#     'city_3' : 9003,
#     'city_4' : 9004,
#     'city_5' : 9005,
# })
#
# data = pd.DataFrame({'area' : a, 'pop' : p})
# #index is sum Nan = not a number
# #print(data)
#
# # 3 =========================================================
#
# dfA = pd.DataFrame(rnd.integers(0, 10, (2, 2)), columns = ['a', 'b'])
# dfB = pd.DataFrame(rnd.integers(0, 10, (3, 3)), columns = ['a', 'b', 'c'])
# print(dfA)
# print(dfB)
# print(dfA + dfB) #Nan + num = Nan

# rng = np.random.default_rng(1)
#
# A = rng.integers(0, 10, (3, 4))
# # print(A)
# # print(A - A[0]) #транслирование
#
# df = pd.DataFrame(A, columns=['a', 'b', 'c', 'd'])
# print(df)
# print(df - df.iloc[0]) #транслирование как в pandas + Ind
#
# print(df.iloc[0, ::2])
#
# print(df - df.iloc[0, ::2])
# согласование индексов - остальные (где нет во стором индексе - Nan )

# 4========================================================

# Pandas - 2 способа хранения отсутствующих значений
# индикаторы  Nan, None
# просто null

# None - обьект (накладные расходы), не работает с sim, min ...

# val1 = np.array([1, None, 3])
# #print(val1.sum()) - error - исключение
#
# val2 = np.array([1, np.nan, 3])
# print(val2.sum()) #нет ошибки, но результат не корректный
# print(np.nansum(val2)) #нет ошибки np.nan = 0
#
# x = pd.Series(range(10), dtype = int)
# print(x)
# x[0] = None #потом станет NaN
# x[1] = np.nan
#
# print(x)
#
# x1 = pd.Series(['a', 'b', 'c'])
# print(x1)
#
# x1[0] = None #потом станет None - типа строка уже обьект не примитивный
# x1[1] = np.nan
# print(x1)
#
# x2 = pd.Series([1, 2, 3, np.nan, None, pd.NA])
# x3 = pd.Series([1, 2, 3, np.nan, None, pd.NA], dtype = 'Int32')
# print(x2)
# print(x3) #тут все налы приводятся к NA
#
# print(x3.isnull()) #bool array
# print(x3.notnull()) #bool array
#
#
# print(x3.dropna())
#
# df = pd.DataFrame([
#     [1, 2, 3, np.nan, None, pd.NA],
#     [1, 2, 3, 4, 5, 6],
#     [1, np.nan, 3, 4, np.nan, 6],
# ])
# print(df)
# print("")
# print(df.dropna()) #одна строка axis = 0
# print("")
# print(df.dropna(axis = 0))
# print("")
# print(df.dropna(axis = 1))

# how - all, все значения NA

# df = pd.DataFrame([
#     [1, 2, 3, np.nan, None, pd.NA],
#     [1, 2, 3, None, 5, 6],
#     [1, np.nan, 3, np.nan, np.nan, 6],
# ])
# print("----------")
# print(df)
# print(df.dropna(axis = 1, how = 'all'))
# print("----------")
# print(df.dropna(axis = 0, how = 'any'))
# print("------------------")
# print(df.dropna(axis = 0, thresh = 2)) # минимум 2 не пустых

# 5===============================================
