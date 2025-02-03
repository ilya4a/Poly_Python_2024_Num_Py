import pandas as pd
import numpy as np

# 1. Разобраться как использовать мультииндексные ключи в данном примере
index = [
    ('city_1', 2010),
    ('city_1', 2020),
    ('city_2', 2010),
    ('city_2', 2020),
    ('city_3', 2010),
    ('city_3', 2020),
]

population = [
    101,
    201,
    102,
    202,
    103,
    203,
]

pop_df = pd.DataFrame(
    {
        'total': population,
        'something': [
            10,
            11,
            12,
            13,
            14,
            15,
        ]
    }, index=pd.MultiIndex.from_tuples(index)
)

# print(pop_df)
pop_df_1 = pop_df.loc['city_1', 'something']
pop_df_2 = pop_df.loc[['city_1', 'city_3'], ['total', 'something']]
pop_df_3 = pop_df.loc[['city_1', 'city_3'], 'something']

# print(pop_df_1, type(pop_df_1))
# print("---------")
# print(pop_df_2, type(pop_df_2))
# print("---------")
# print(pop_df_3, type(pop_df_3))


# ----------------------------------------------------------------------------

# 2. Из получившихся данных выбрать данные по
# - 2020 году (для всех столбцов)
# - job_1 (для всех строк)
# - для city_1 и job_2

index = pd.MultiIndex.from_product([
    ['city_1', 'city_2'],
    [2010, 2020]
], names=['city', 'year'])

# print(index)

columns = pd.MultiIndex.from_product([
    ['person_1', 'person_2', 'person_3'],
    ['job_1', 'job_2']
], names=['worker', 'job'])

# print(columns)

rng = np.random.default_rng(1)

data = rng.random((4, 6))
# print(data)

df = pd.DataFrame(data, index=index, columns=columns)

# print(df)
# print("------------")
# #print(df.loc[:, 2020, :])
# print(df.loc[(["city_1", "city_2"], 2020), ()]) #1
# print("----------------------")
# print(df.loc[(["city_1", "city_2"], [2010, 2020]), (["person_1", "person_2", "person_3"], "job_1")]) #2
# print("----------------------")
# print(df.loc[("city_1", [2010, 2020]), (["person_1", "person_2", "person_3"], "job_2")]) #3


# 3. Взять за основу DataFrame со следующей структурой
index = pd.MultiIndex.from_product(
    [
        ['city_1', 'city_2'],
        [2010, 2020]
    ],
    names=['city', 'year']
)
columns = pd.MultiIndex.from_product(
    [
        ['person_1', 'person_2', 'person_3'],
        ['job_1', 'job_2']
    ],
    names=['worker', 'job']
)

data = rng.random((4, 6))
df = pd.DataFrame(data, index=index, columns=columns)
# Выполнить запрос на получение следующих данных
# - все данные по person_1 и person_3
# - все данные по первому городу и первым двум person-ам (с использование срезов)
#
# Приведите пример (самостоятельно) с использованием pd.IndexSlice

df1_0 = df.loc[:, pd.IndexSlice[['person_1', 'person_3'], :]]
df2_0 = df.loc[pd.IndexSlice['city_1', :], pd.IndexSlice[:'person_2', :]]

df1_1 = df.loc[:, (["person_1", "person_3"])]
df2_1 = df.loc[("city_1", [2010, 2020]), (["person_1", "person_2"])]

# print(df1_0, df2_0, df1_1, df2_1, sep="\n-------------\n")


# 4. Привести пример использования inner и outer джойнов для Series (данные примера скорее всего нужно изменить)
# ser1 = pd.Series(['a', 'b', 'c'], index=[1,2,3])
# ser2 = pd.Series(['b', 'c', 'f'], index=[3,5,6])
#
# print (pd.concat([ser1, ser2], join='outer', axis=1))
# print("-----------------------")
# print (pd.concat([ser1, ser2], join='outer', axis=1, ignore_index=True))
# print("-----------------------")
# print (pd.concat([ser1, ser2], join='outer', axis=0))
# print("-----------------------")
# print (pd.concat([ser1, ser2], join='outer', axis=0, ignore_index=True))
# print("-----------------------")
#
# print("inner: ")
#
# ser1 = pd.Series(['a', 'b', 'c'], index=[1,2,3])
# ser2 = pd.Series(['a', 'b', 'f'], index=[3,5,6])
#
# print (pd.concat([ser1, ser2], join='inner', axis=1)) # c a
# print("----")
# print (pd.concat([ser1, ser2], join='inner', axis=1, ignore_index=True))
# print("---")
# print (pd.concat([ser1, ser2], join='inner', axis=0))
#
# ser1 = pd.Series(['a', 'b', 'c'], index=[1,2,3])
# ser2 = pd.Series(['d', 'e', 'f'], index=[1,2,3])
#
# print("-----")
# print (pd.concat([ser1, ser2], join='inner', axis=1)) # all
# print (pd.concat([ser1, ser2], join='inner', axis=0)) # all
#
# print("---")
# ser1 = pd.Series(['a', 'b', 'c'], index=[1,2,3])
# ser2 = pd.Series(['d', 'e', 'f'], index=[4, 5, 6])
# print (pd.concat([ser1, ser2], join='inner', axis=1)) # empty
# print (pd.concat([ser1, ser2], join='inner', axis=0)) # all
