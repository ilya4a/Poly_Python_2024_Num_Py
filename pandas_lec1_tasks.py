import numpy as np
import pandas as pd

# 1. Привести различные способы создания объектов типа Series
# Для создания Series можно использовать
# - списки Python или массивы NumPy
# - скалярные значение
# - словари

# 1.1
print(pd.Series(['a', 'b', 'c']))
print(pd.Series(np.array(['a', 'b', 'c'])))

# 1.2
print(pd.Series(1, index=['a', 'b', 'c']))

# 1.3
print(pd.Series({'a': 1, 'b': 2, 'c': 3}))

# 2. Привести различные способы создания объектов типа DataFrame
# DataFrame. Способы создания
# - через объекты Series
# - списки словарей
# - словари объектов Series
# - двумерный массив NumPy
# - структурированный массив Numpy

# 2.1
print(pd.DataFrame([pd.Series([1, 2, 3]), pd.Series([4, 5, 6])]))

# 2.2
print("\n-----\n", pd.DataFrame([{'a': 1, 'b': 2, 'c': 3}, {'a': 4, 'b': 5, 'c': 6}]))

# 3.3
s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s2 = pd.Series([4, 5, 6], index=['a', 'b', 'c'])
print(pd.DataFrame({
    'col1': s1,
    'col2': s2
}), '\n----------')

# 3.4
print(pd.DataFrame(np.random.randint(0, 100, (4, 5))))

# 3.5
data = np.zeros(4, dtype={
    'names': [
        'name', 'age'
    ],
    'formats': [
        'U10', 'i4'
    ]
})
data['name'] = np.array(['name1', 'name2', 'name3', 'name4'])
data['age'] = np.array([10, 20, 30, 40])
print(pd.DataFrame(data, index=['a', 'b', 'c', 'd']), "\n --------------")

# 3. Объедините два объекта Series с неодинаковыми множествами ключей (индексов) так, чтобы вместо NaN было установлено значение 1

s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c1', 'd'])
s2 = pd.Series([4, 5, 6], index=['a', 'b', 'c'])
print((s1 + s2).fillna(1))  # меняем на 1 после сложения
print((s1.add(s2, fill_value=1)), '\n---------------------')  # меняем на 1 перед сложением

# 4. Переписать пример с транслирование для DataFrame так, чтобы вычитание происходило по СТОЛБЦАМ

rng = np.random.default_rng(1)
A = rng.integers(0, 10, (3, 4))
df = pd.DataFrame(A, columns=['a', 'b', 'c', 'd'])
print(df)
print(df - df.iloc[0])
print(df.sub(df.iloc[:, 0], axis=0), "\n--------------")

# 5. На примере объектов DataFrame продемонстрируйте использование методов ffill() и bfill()

df = pd.DataFrame([
    [1, 2, 3, np.nan, None, pd.NA],
    [1, 2, 3, None, 5, 6],
    [1, np.nan, 3, np.nan, np.nan, 6],
])
print(df, '\n--------------')
# df.fillna(np.nan, inplace = True)
print(df.ffill(), '\n------------------')  # по строкам, заменяется предыдущим
print(df.ffill(limit=1), '\n------------------')
# print(df.ffill(axis=1)) FutureWarning

print(df.bfill())  # по строкам, заменяется следующим
# print(df.bfill(limit = 1))
# print(df.bfill(axis = 1))
