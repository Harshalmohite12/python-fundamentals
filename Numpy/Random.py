import numpy as np


# print(np.random.randint(1, 11, 10))
# print(np.random.randn())

# np.random.seed(42)
# print(np.random.randint(3,8,9))

# arr = np.arange(1, 11)
# print(arr)
# np.random.shuffle(arr)
# print(arr)


# Randomly generate scores between 50 and 100
np.random.seed(42)
scores = np.random.randint(50, 101, size=(5,4))
print("Scores:\n", scores)

# print(np.mean(scores, axis=1))
# print(np.mean(scores, axis=0))

students_all_above_80 = scores[np.all(scores > 60, axis=1)]
# print(students_all_above_80)

scores = scores + 5
# print(scores)

weights = np.array([0.25, 0.25, 0.25, 0.25])
scores = scores * weights
print(scores)



