import numpy as np

array = np.array([[1, 2, 3, 4], 
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]
                  ])

# array[start: end: step]

# print(array[0])  # To print desired row
# print(array[:, 0]) # To print desired coloumn
# print(array[0,0]) # To print desired item from matrix
# print(array[1:3, 1:3]) # To print deesired matrix from main matrix

# print(array[0:4:2])
# print(array[:, 0:3:2])
# print(array[2: ,  1:3])

m = np.arange(1, 13).reshape(3, 4)
# print(m)

# m =
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

# print(m[2,1])
# print(m[:, -1])
# print(m[0:2])
# print(m[:, 2:4])
# print(m[0:2, 1:3])
# print(m[1:3, 2:4])
print(m[::-1, :])
print(m[:, ::-1])
