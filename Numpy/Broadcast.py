import numpy as np

# array1 = np.array([5, 3, 9, 1])
# array2 = np.array([[1], 
#                    [2], 
#                    [3], 
#                    [4]])
# print(array1.shape)
# print(array2.shape)
# print(array1 + array2)


# scores = np.array([
#     [85, 90, 78],
#     [88, 76, 92],
#     [79, 85, 80]
# ])

# weights = np.array([0.3, 0.4, 0.3])

# print("Scores with weights: ")
# print(scores * weights)
# print((scores * weights).sum(axis=1))

array1 = np.array([[1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10]])
# array2 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])

# print(array1.shape)
# print(array2.shape)

# print(array1 * array2)

# print(np.sum(array1))
# print(np.mean(array1))
# print(np.std(array1))
# print(np.var(array1))
# print(np.max(array1))
# print(np.min(array1))
# print(np.argmax(array1))
# print(np.argmin(array1))

# print(np.sum(array1, axis=0))
# print(np.sum(array1, axis=1))

# a = np.array([[1,2,3],[4,5,6]])
# b = np.array([[10,20,30]])

# print(a + b)  
# # [[11 22 33]
# #  [14 25 36]]
# print(a.shape)
# print(b.shape)

m = np.arange(1, 13).reshape(3, 4)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

# print(m[[0, 2]])
# print(m[:, [1, 3]])

# n = np.array([100, 200, 300, 400])
# n = np.array([[1],[2],[3]])
# print(m + n)

# sub_array = (m[[0,1], :][:, [1,2]])
# add_array = np.array([10, 20])
# print(sub_array + add_array)

# n = np.array([[1],[10],[100]])
# print(m * n)

