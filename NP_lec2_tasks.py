import numpy as np
import sys
import array
import random
import matplotlib.pyplot as plt

## 1. Что надо изменить в последнем примере, чтобы он заработал без ошибок (транслирование)?
a = np.ones((3, 2))
b = np.arange(3)
c = np.nan

try:
    c = a + b
except Exception as e:
    print(e.args)

a = np.ones((3, 2))
b = np.arange(3)[:, np.newaxis]
c = a + b
print(c, '\n-----')

## 2. Пример для y. Вычислить количество элементов (по обоим размерностям), значения которых больше 3 и меньше 9

x = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(np.sum(np.multiply(x > 3, x < 9)))
print(np.sum(np.multiply(x > 3, x < 9), axis=0))
print(np.sum(np.multiply(x > 3, x < 9), axis=1))
