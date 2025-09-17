import numpy as np


# arr = np.arange(12).reshape(3, 4)

# print(arr)
# print(arr.shape)     
# print(arr.ndim)      
# print(arr.dtype)    
# print(arr.size)     
# print(arr.itemsize)  
# print(arr.nbytes)   

# big_arr = np.arange(1000000, dtype=np.float64)

# big32 = big_arr.astype(np.float32) 
# print(big32.nbytes)

# a = np.arange(10)
# print(a.dtype)
# print(a)
# b = a.astype(np.float32)
# print(b)
# print(b.dtype)
# c = b.astype(np.int16)
# print(c.dtype)
# print(c)


# array = np.array([2, 4, 5, 7, 9])
# array *= 2
# print(array)
# print(type(array))

# array = np.array("A")
# print(array.ndim)

# array = np.array(["A", "B", "C"])
# print(array.ndim)

# array = np.array([["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]])
# print(array.ndim)

array = np.array([[["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]],
                  [["J", "K", "L"], ["M", "N", "O"], ["P", "Q", "R"]],
                  [["S", "T", "U"], ["V", "W", "X"], ["Y", "Z", " "]]
                  ])
# print(array.ndim)
# print(array.shape)
# print(array[0][0][0])  # Chain Indexing
# print(array[0, 0, 0])  # MultiDimesitional Indexing
# print(array[0, 1, 0])
# print(array[0, 0, 2])
# print(array[1, 0, 0])
# print(array[2, 2, 2])

word = array[0, 0, 2] + array[0, 0, 0] + array[1, 2, 2]
# print(word)