import numpy as np
import sys
import array
import random

x = 1
# print(sys.getsizeof())
x = True
# print(type(x))

l1 = list([])
l2 = list([1, "2", True])

# print(sys.getsizeof(l1),sys.getsizeof(l2))

'''
a1 = array.array('i', [1, 2, 3])
#'I'| unsigned int | int
#'d' double
#'q' signed long long
a3 = array.array('d', [1.4, 2, 3])
print(sys.getsizeof(a3), type(a1))'''

a = np.array([1, 2, 3, 4])
# print(type(a), a)

a2 = np.array([1, 2, 3, 4.1], dtype=int)
# print(type(a2), a2)

a = np.array([range(i, i + 3) for i in [2, 4, 6]])
# print(a, type(a))

# print(np.zeros(10, dtype = int))
# print(np.ones((3, 5), dtype = float) )
# print(np.full((3, 5), 77, dtype = float) )
# print(np.arange(0, 20, 2, dtype = float) )
# print(np.eye(2, dtype = float) )

# print(np.random.rand(5)) #3


# print(np.random.normal(0, 1, 10)) #5
# print(np.random.randint(10, size = 5)) #6

# np.random.seed(5)

x1 = np.random.randint(10, size=3)
x2 = np.random.randint(10, size=(3, 2, 2))
# print(x1, '\n', x2)

# print(x1.ndim, x1.shape, x1.size)
# print(x2.ndim, x2.shape, x2.size)

a = np.array([1, 2, 3, 4, 5])
a[1] = 100
# print(a[-4])

a = np.array([[1, 2], [3, 4]])
a[-1, -1] = 100
# print(a[-1, -1])

a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 2.4, 3, 4])

# print(a)
# print(b)
#
# a[0] = 10
# print(a)
#
# a[0] = 0.1
# print(a) #тип фиксируется!!!!

a = np.array([1, 2, 3, 4])
# print(a[0:3:1])
# print(a[:3])
# print(a[1:3])

# -----------------
a = np.array([range(i, i + 3) for i in range(4)])  # 7
# print(a)
# print(a[:2, :3])
# print(a[:3, 1:2])
# print(a[::-1, ::-1])
# print(a[::, 1:2])
# print(a[2:3, ::])


a = np.array([1, 2, 3])
b = a[1:]
b[0] = -10
# print(a)

# ------------------------
# 8
a = np.array([1, 2, 3])
b = a[1:].copy()
b[0] = -10
# print(a)
# ----------------------

a = np.arange(1, 13)
# print(a)
# print(a.reshape(2, 6))

# ------------------
# 9
a = np.array([1, 2, 3])
# print(a[:, np.newaxis])
# print(a[np.newaxis, :])
# ----------------

x = np.array([1, 2, 3])
y = np.array([4, 5])
z = np.array([6])

# print(np.concatenate([x, y, z]) )

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
r1 = np.vstack((x, y))
# print(r1)

# print(np.hstack([r1, r1]))
# print(np.hstack([x, x]))

x2 = np.array([7, 8, 9])
y2 = np.array([12, 11, 10])

r2 = np.vstack((x2, y2))
# print(r2)
# ------------------
# 10
# print(np.dstack([r1, r2])) # для 3 измерений все особенно логично
# ---------------------
# 11
# a = np.array([1, 2, 3, 4, 5, 6]).reshape(2, 3)
# #print(np.split(a, 2))
# print(np.vsplit(a, 2))
# a = np.array([1, 2, 3, 4, 5, 6]).reshape(3, 2)
# print(np.hsplit(a, 2))
#
# x = np.arange(16.0).reshape(2, 2, 4)
# x = np.dsplit(x, 2)
# print(x)

x = np.arange(10)
# print(x*2 + 1)
# print(np.add(np.multiply(x, 2), 1))
# - - / // ** %

# --------------------
# 12
# x = np.arange(10)
# print(x - 10)
# print(-x)
# print(x / 2)
# print(x //2)
# print(x**2)
# print(x % 2)
# ----------------------

x = np.arange(5)
y = np.zeros(10)
np.multiply(x, 10, out=y[::2])
# print(y)

# x = np.arange(1, 5)
# print(np.add.reduce(x))
# print(np.add.accumulate(x))

x = np.arange(1, 10)
# print(np.add.outer(x, x))
# print(np.multiply.outer(x, x))
