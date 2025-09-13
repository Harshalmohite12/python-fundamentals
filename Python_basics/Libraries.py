# 📌 Python Import Cheat Sheet

## 🔹 1. Import entire module
# import math
# print(math.sqrt(16))   # 4.0
# print(math.pi)         # 3.141592653589793
# ```



# ## 🔹 2. Import with alias (shortcut name)
# import math as m
# print(m.sqrt(25))   # 5.0
# print(m.pi)         # 3.141592653589793
# ```



# ## 🔹 3. Import specific functions/variables
# from math import sqrt, pi
# print(sqrt(36))   # 6.0
# print(pi)         # 3.141592653589793
# ```


# ## 🔹 4. Import everything (⚠️ avoid in big projects)
# from math import *
# print(sqrt(49))   # 7.0
# print(pi)         # 3.141592653589793
# ```


# ## 🔹 5. Import your own file (custom module)
# 📁 Suppose file `mymath.py`:
# def add(a, b):
#     return a + b


# 📁 Another file:
# import mymath
# print(mymath.add(10, 20))   # 30

# Or:

# from mymath import add
# print(add(10, 20))   # 30


# ## 🔹 6. ML-style imports (commonly used)
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# # Example
# arr = np.array([1, 2, 3])
# print(arr)

# df = pd.DataFrame({"name": ["Harshal", "Shweta"], "marks": [90, 95]})
# print(df)

# plt.plot([1, 2, 3], [4, 5, 6])
# plt.show()



# ✅ **Golden Rule**:

# * Use **alias** for big libraries (`np`, `pd`, `plt`).
# * Use `from ... import ...` for specific functions you use a lot.
# * Avoid `from ... import *` (confusing in large projects).
