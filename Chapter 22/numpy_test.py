# import numpy as np

# b = np.array( [2, 4, 6, 8] )
# print(b)
# print(b.ndim)
# print(b.size)
# print(b.shape)


# import numpy as np

# a = np.arange(10)
# print(a)
# print(a.ndim)
# print(a.shape)
# print(a.size)

# a = np.arange(7, 11)
# print(a)

# a = np.arange(7, 11, 2)
# print(a)

# f = np.arange(2.0, 9.8, 0.3)
# print(f)

# # g = np.arange(10, 4, -1.5, dtype=np.float)
# # print(g)


# import numpy as np

# a = np.zeros((3,))
# print(a)
# print(a.ndim)
# print(a.shape)
# print(a.size)

# b = np.zeros((2, 4))
# print(b)
# print(b.ndim)
# print(b.shape)
# print(b.size)

# k = np.ones((3, 5))
# print(k)

# # m = np.random.random((3, 5))
# # print(m)


# import numpy as np

# a = np.arange(10)
# print(a)
# a = a.reshape(2, 5)
# print(a)
# print(a.ndim)
# print(a.shape)
# print(a.size)

# a = a.reshape(5, 2)
# print(a)
# print(a.ndim)
# print(a.shape)
# print(a.size)

# # a.shape = (2, 5)
# # print(a)

# # a = a.reshape(3, 4)


# import numpy as np

# a = np.arange(10)
# print(a[7])
# print(a[-1])

# a = a.reshape(2, 5)
# print(a)
# print(a[1, 2])

# l = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
# print(l)
# # print(l[1, 2])
# print(l[1][2])

# a = np.arange(10)
# a = a.reshape(2, 5)
# print(a)
# print(a[0, 2:])
# print(a[-1, :3])

# a[:, 2:4] = 1000
# print(a)


# from numpy import *

# a = arange(4)
# print(a)
# a *= 3
# print(a)


# plain_list = list(range(4))
# print(plain_list)
# plain_list = [num * 3 for num in plain_list]
# print(plain_list)

# a = zeros((2, 5)) + 17.0
# print(a)


import numpy as np

coefficients = np.array([[4, 5], [1, 2]])
dependents = np.array([20, 13])

answers = np.linalg.solve(coefficients, dependents)
print(answers)

print(4 * answers[0] + 5 * answers[1])
print(1 * answers[0] + 2 * answers[1])

product = np.dot(coefficients, answers)
print(product)

print(np.allclose(product, dependents))