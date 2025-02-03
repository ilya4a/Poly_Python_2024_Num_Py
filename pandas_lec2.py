import pandas as pd
import numpy as np

# index = [
#     ('city_1', 2001),
#     ('city_1', 2012),
#     ('city_3', 2001),
#     ('city_3', 2012),
#     ('city_4', 2004),
#     ('city_5', 2005),
#     ('city_6', 2006),
#     ('city_7', 2007),
# ]
#
# population = [101, 201, 103, 202, 203, 204, 205, 210]
#
# p = pd.Series(population, index = index)
# print(p)
#
# print(p[ [i for i in p.index if i[1] == 2003] ])
# #Multuindex
#
# index = pd.MultiIndex.from_tuples(index)
#
# p = p.reindex(index)
# print(p[:, 2001])
#
# p_df = p.unstack() # переходим к DataFrame
# print(p_df)
# print(p_df.stack()) # back

# index = [
#     ('city_1', 2001, 1),
#     ('city_1', 2001, 2),
#
#     ('city_1', 2012, 1),
#     ('city_1', 2012, 2),
#
#     ('city_3', 2001, 1),
#     ('city_3', 2001, 2),
#
#     ('city_3', 2012, 1),
#     ('city_3', 2012, 2),
# ]
#
# population = [101, 201, 103, 202, 203, 204, 205, 210]
#
# p = pd.Series(population, index = index)
# index = pd.MultiIndex.from_tuples(index)
# p = p.reindex(index)
# print(p[:, 2012])
# print(p[:, :, 2])
# p_df = p.unstack()
# print(p_df) #последнее измерение индекса - колонки
# print(p_df.stack())


# ind = [
#     ('city_1', 2001, 1),
#     ('city_1', 2001, 2),
#
#     ('city_1', 2012, 1),
#     ('city_1', 2012, 2),
#
#     ('city_3', 2001, 1),
#     ('city_3', 2001, 2),
#
#     ('city_3', 2012, 1),
#     ('city_3', 2012, 2),
# ]
# population = [101, 201, 103, 202, 203, 204, 205, 210]
#
# index = pd.MultiIndex.from_tuples(ind)
# p = pd.Series(population, index = index)
#
# p_df = pd.DataFrame({
#     'total' : p,
#     'smth' : [1, 2, 3, 4, 5, 6, 7, 8]
# })
# #print(p_df['smth'])
# print(p_df)


# p_df_1 = p_df.loc["city_1", 1,]
# print(p_df_1)
# print(p_df.loc)
# 1===================================== получить по loc? 52.24

# как можно создавать мультииндексы

# список массивов
# 1)
# index1 = pd.MultiIndex.from_arrays([
#     ['a', 'a', 'b', 'b'],
#     [1, 2, 1, 2]
# ])
# print(index1)
#
# #2) list of tuples
# index2 = pd.MultiIndex.from_tuples([
#     ('a', 1),
#     ('a', 2),
#     ('b', 1),
#     ('b', 2)
# ])
#
# #2)декартово произведение обычных индексов
#
# index3 = pd.MultiIndex.from_product([
#     ['a', 'b'],
#     [1, 2]
# ])
# print(index3)
#
# #4) описание внутреннго представления levels, codes
#
# index4 = pd.MultiIndex(
#     levels = [
#         ['a', 'b', 'c'],
#         [1, 2]
#     ],
#     codes=[
#         [0, 0, 1, 1, 2, 2], #a a b b c c
#         [0, 1, 0, 1, 0, 1]  #1 2 1 2 1 2
#     ]
# )
# print(index4)
#
# #names of levels
#
# data = {
#     ('city_1', 2010) : 100,
#     ('city_1', 2020) : 101,
#     ('city_2', 2010) : 1001,
#     ('city_2', 2020) : 1002,
# }
#
# s = pd.Series(data)
# print("--------------------")
# print(s)
# print("--------------------")
#
# s.index.names = ['city', 'year']
# print(s)


# index = pd.MultiIndex.from_product([
#     ['city_1', 'city_2'],
#     [2001, 2010]
# ], names =['city', 'year'])
#
# print(index)
#
# columns = pd.MultiIndex.from_product([
#     ['person_1', 'person_2', 'person_3'],
#     ['job_1', 'job_2']
# ], names =['worker', 'job'])
#
# print(columns)
#
# rng = np.random.default_rng(1)
#
# data = rng.random((4, 6))
# print(data)
#
# df = pd.DataFrame(data, index=index, columns=columns)
# print("---------------------")
# print(df)

# 2======================================== 34 26


# Индексация и срезы

# data = {
#     ('city_1', 2010) : 100,
#     ('city_1', 2020) : 101,
#     ('city_2', 2010) : 1001,
#     ('city_2', 2020) : 1002,
#     ('city_3', 2010) : 3002,
#     ('city_3', 2020) : 3002,
# }
#
# s = pd.Series(data)
# s.index.names = ['city', 'year']
#
# print(s['city_1', 2010])
# print(s['city_1'])
#
# print(s['city_1'])
#
# print(s.loc['city_1' : 'city_2'])
# print(s[s > 1000])
# print("----------------------")
# print(s[['city_1', 'city_3']])

# 3============================================================

# rng = np.random.default_rng(1)
#
# index = pd.MultiIndex.from_product([
#     ['a', 'c','b'],
#     [2, 1]
# ])
#
# data = pd.Series(rng.random(6), index= index)
# data.index.names = ['char', 'int']
# print(data)
# #print(data['a':'b']) error - not sort
#
# data = data.sort_index()
# print(data['a':'b'])


# index = [
#     ('city_1', 2001, 1),
#     ('city_1', 2001, 2),
#
#     ('city_1', 2012, 1),
#     ('city_1', 2012, 2),
#
#     ('city_3', 2001, 1),
#     ('city_3', 2001, 2),
#
#     ('city_3', 2012, 1),
#     ('city_3', 2012, 2),
# ]
#
# population = [101, 201, 103, 202, 203, 204, 205, 210]
#
#
# pop = pd.Series(population, index = index)
# print(pop)
# i = pd.MultiIndex.from_tuples(index)
# pop = pop.reindex(i)
# print(pop)
# print(pop.unstack())
# print("----------------")
# print(pop.unstack(level=0)) # columns - city
# print(pop.unstack(level=1)) #[1]...
# print(pop.unstack(level=2))


# NumPy сонкатинация

x = [[1, 2, 3]]
y = [[4, 5, 6]]
z = [[7, 8, 9]]

print(np.concatenate([x, y, z]))
print(np.concatenate([x, y, z], axis=0))
print(np.concatenate([x, y, z], axis=1))

# Pandas concat

ser1 = pd.Series(['a', 'b', 'c'], index=[1, 2, 3])
ser2 = pd.Series(['d', 'e', 'f'], index=[1, 5, 6])

print(pd.concat([ser1, ser2], verify_integrity=False))
print(pd.concat([ser1, ser2], ignore_index=True))
print(pd.concat([ser1, ser2], keys=['x', 'y']))

ser1 = pd.Series(['a', 'b', 'c'], index=[1, 2, 3])
ser2 = pd.Series(['b', 'c', 'f'], index=[1, 5, 6])

print("------------------------")

print(pd.concat([ser1, ser2], join='outer'))
print(pd.concat([ser1, ser2], join='inner'))

# 4============================================================== 3.40
