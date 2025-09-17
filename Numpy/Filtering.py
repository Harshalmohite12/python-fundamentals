import numpy as np

m = np.arange(1, 13).reshape(3, 4)
print(m[m<5])
print(m[m % 2 == 0])
print(m[(m > 3) & (m < 10)])
print(m[m % 3 != 0])
