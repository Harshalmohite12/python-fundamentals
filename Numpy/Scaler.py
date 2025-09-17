import numpy as np

#SCALAR ARTHMATIC

array = np.array([1, 2, 3])

# print(array + 1)
# print(array - 2)
# print(array * 3)
# print(array / 4)
# print(array ** 5)

#VECTORIZED MATH FUNCTION

array1 = np.array([1.2, 4.23, 3.53])

# print(np.sqrt(array1))
# print(np.floor(array1))
# print(np.ceil(array1))
# print(np.pi)

# print(array + array1)
# print(array - array1)
# print(array * array1)
# print(array / array1)


#LITTLE EXERCISE

# radi = np.array([4, 6, 2])
# print("Area: ", np.pi * radi ** 2)

#Comparison Operators
Scores = np.array([23, 98, 76, 100, 67, 87])

# print(Scores == 100)
# print(Scores >= 60)
# print(Scores < 60)

Scores[Scores < 60] = 0
# print(Scores)


# a = np.array([[1, 2],
#              [3, 4]])

# b = np.array([[5, 6],
#              [7, 8]])

# print(a + b)
# print(a - b)
# print(a * b)
# print(a.T)
# print(np.linalg.inv(a))
# print(a @ b)          # using @ operator
# print(np.dot(a, b))   # using np.dot

