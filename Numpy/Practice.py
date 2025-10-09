import numpy as np

# np.random.seed(12)
# ran_list =np.random.randint(50, 100, 20)
# # print(ran_list)
# arr = np.array([ran_list]).reshape(4,5)
# print(arr)
# print("Marks of student 1: ", arr[0], "Percentage Marks : ", np.mean(arr[0]), "Highest score: ", np.max(arr[0]))
# print("Marks of student 2: ", arr[1], "Percentage Marks : ", np.mean(arr[1]), "Highest score: ", np.max(arr[1]))
# print("Marks of student 3: ", arr[2], "Percentage Marks : ", np.mean(arr[2]), "Highest score: ", np.max(arr[2]))
# print("Marks of student 4: ", arr[3], "Percentage Marks : ", np.mean(arr[3]), "Highest score: ", np.max(arr[3]))

# [[68 98 60 66 88] 
#  [84 75 94 85 76] 
#  [52 96 87 63 60] 
#  [59 61 52 82 69] 
#  [71 69 61 72 61] 
#  [51 68 74 78 61]]
np.random.seed(13)
marks = np.random.randint(50, 101, 30).reshape(6, 5)
# print(marks)
# print(marks[2])
# print(marks[:, -1])

# for i in range(6):
#     student_marks = marks[i]
#     print("Average marks of student ", i+1, "is ", np.mean(student_marks))
    
# for i in range(5):
#     subject_marks = marks[:, i]
#     print("Average marks of subject ", i+1, "is ", np.mean(subject_marks))
    
# print(marks[marks > 90])
# student_above_70 = marks[np.all(marks > 70, axis=1)]
# print(student_above_70)

# if True:
#     marks[marks < 60] = 60
    
# print(marks)

# first_subject = marks[:, 0]
# print(first_subject)
# print(first_subject[first_subject < 70])

# count = 0
# count = marks[(marks < 85) & (marks > 65)]  
# print(len(count), "students scores between 85 to 65")


# print(marks + 5)

# print(marks * 0.5)

# marks[:, 0] = marks[:, 0] - 10
# print(marks)

# marks[:, 0:4] = marks[:, 0:4] + 5
# print(marks)

# marks[1:5, -1] = marks[1:5, -1] * 1.1
# print(marks)

# weight_array = [0.2, 0.2, 0.2, 0.2, 0.2]
# print(marks * weight_array)

# avg_marks = np.mean(marks, axis=1, keepdims=True)
# print(avg_marks)

# print(marks - avg_marks)

# print(marks)
# highest_marks = np.max(marks, axis = 1)
# print(highest_marks)
# lowest_marks = np.min(marks, axis= 1)
# print(lowest_marks)

# diff_marks = highest_marks - lowest_marks
# print(diff_marks)


# def strStr(haystack, needle):
#     if needle in haystack:
#         return haystack.find(needle)
#     else :
#         return -1
    
# print(strStr("sadisad", "sad"))
# print(strStr("issadnotsad", "sad"))
# print(strStr("leetcode", "codes"))


np.random.seed(7)
arr = np.random.randint(50, 101, 30).reshape(6, 5)
# print(arr)
# [[97 54 75 53 69]
#  [73 89 78 64 73]
#  [58 75 96 92 76]
#  [58 89 88 54 98]
#  [57 94 50 61 56]
#  [69 94 55 74 98]]
arr[arr < 60] = 60
# print(arr)
# [[97 60 75 60 69]
#  [73 89 78 64 73]
#  [60 75 96 92 76]
#  [60 89 88 60 98]
#  [60 94 60 61 60]
#  [69 94 60 74 98]]
highest_score = np.mean(arr, axis=1)
print(np.round(highest_score))
highest_scored_student = np.max(highest_score)
highest_scored_student_id = np.argmax(highest_score)

print(f"The roll numnber {np.round(highest_scored_student_id + 1)} student scored highest average marks. Average marks :{np.round(highest_scored_student)}")

lowest_score = np.mean(arr, axis=0)
print(np.round(lowest_score))
lowest_scored_subject = np.min(lowest_score)
lowest_scored_subject_id = np.argmin(lowest_score)

print(f"Lowest averaged subject : {np.round(lowest_scored_subject_id)} AND Averge : {np.round(lowest_scored_subject)}")

subject_3 = arr[:, 2]
print(subject_3)
subject_3[subject_3 > 90] += 2
print(subject_3)