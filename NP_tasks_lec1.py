import numpy as np
import sys
import array
import random

# Лемдянов Илья

## 1. Какие еще существуют коды типов?
a1 = array.array('i', [1, 2, 3])
# 'I'| unsigned int
# 'd' double
# 'q' signed long long
# 'd' double
# 'b' signed char

## 2. Напишите код, подобный приведенному выше, но с другим типом
a3 = array.array('d', [1.4, 2, 3])
# print(sys.getsizeof(a3), type(a1))

## 3. Напишите код для создания массива с 5 значениями, располагающимися через равные интервалы в диапазоне от 0 до 1
# print(np.arange(0, 10, 2) / 10)

## 4. Напишите код для создания массива с 5 равномерно распределенными случайными значениями в диапазоне от 0 до 1
# print(np.random.rand(5))


## 5. Напишите код для создания массива с 5 нормально распределенными случайными значениями с мат. ожиданием = 0 и дисперсией 1
# print(np.random.normal(0, 1, 5))

## 6. Напишите код для создания массива с 5 случайнвми целыми числами в от [0, 10)
# print(np.random.randint(0, 10, size=5))


## 7. Написать код для создания срезов массива 3 на 4
## - первые две строки и три столбца
## - первые три строки и второй столбец
## - все строки и столбцы в обратном порядке
## - второй столбец
## - третья строка

a = np.array([range(i, i + 3) for i in range(4)])  # 7
# print(a)
# print(a[:2, :3])
# print(a[:3, 1:2])
# print(a[::-1, ::-1])
# print(a[::, 1:2])
# print(a[2:3, ::])


## 8. Продемонстрируйте, как сделать срез-копию
a = np.array([1, 2, 3])
b = a[1:].copy()
b[0] = -10
# print(a)

## 9. Продемонстрируйте использование newaxis для получения вектора-столбца и вектора-строки
a = np.array([1, 2, 3])
# print(a[:, np.newaxis])
# print(a[np.newaxis, :])

## 10. Разберитесь, как работает метод dstack
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
r1 = np.vstack((x, y))

x2 = np.array([7, 8, 9])
y2 = np.array([12, 11, 10])
r2 = np.vstack((x2, y2))

# print(np.dstack([r1, r2]))

## 11. Разберитесь, как работают методы split, vsplit, hsplit, dsplit
# a = np.array([1, 2, 3, 4, 5, 6]).reshape(2, 3)
# print(np.split(a, 2))
#
# print(np.vsplit(a, 2))
#
# a = np.array([1, 2, 3, 4, 5, 6]).reshape(3, 2)
# print(np.hsplit(a, 2))
#
# x = np.arange(16.0).reshape(2, 2, 4)
# x = np.dsplit(x, 2)
# print(x)

## 12. Привести пример использования всех универсальных функций, которые я привел
# x = np.arange(10)
# print(x - 10)
# print(-x)
# print(x / 2)
# print(x //2)
# print(x**2)
# print(x % 2)
