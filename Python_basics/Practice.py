# TRICKS
# 1:-to use sum function with any condtion:
#       sum(x for x in collection if condition)
#       for ex nums = (1, 2, 3, 4, 5, 6)
#       even_sum = sum(x for x in nums if x % 2 == 0)
#       print(even_sum)








# name = "Harshal"
# age = 21
# city = "Baramati"
# print(f"my name is {name} and my age is {age} and i live in {city} city")

# movies = ["ironman", "antman",  "captain america"]
# print(movies[0])
# print(movies[len(movies)-1])
# movies.pop(1)
# movies.append("thor")
# print(movies)

# fruits = ("apple", "banana", "guva")
# print(fruits[0])
# print(fruits[len(fruits)-1])

# if "apple" in fruits:
#     print("Apple exists")
    
# fruit1 = fruits[0]
# fruit2 = fruits[1]
# fruit3 = fruits[2]
# print(fruit1)
# print(fruit2)
# print(fruit3)

# numbers = (10, 20, 30, 40, 50, 60)
 
# for i in range(0, 3):
#     print(numbers[i])
    
# print(numbers[-2], numbers[-1])
    
# if 30 in numbers:
#     print("True")

# sum = 0
# for i in numbers:
#     sum += i
    
# print(sum)


# students = ["Harshal", "Shweta", "Chaitanya"]
# Harshal = (80,90,97)
# Shweta = (88,90,97)
# Chaitanya = (80,99,97)

# students = {
#     "Harshal": (80,90,97), 
#     "Shweta": (88,90,97),
#     "Chaitanya": (80,99,97)
# }

# def marking_system(students_dict):
#     topper = None
#     highest_avg = 0
    
#     for name, marks in students_dict.items():
#         avg = sum(marks) / len(marks)
        
#         # Assign grade
#         if avg >= 90:
#             grade = "A"
#         elif avg >= 75:
#             grade = "B"
#         elif avg >= 60:
#             grade = "C"
#         else:
#             grade = "Fail"
        
#         print(f"{name} -> Marks: {marks}, Average: {avg:.2f}, Grade: {grade}")
        
#         # Check for topper
#         if avg > highest_avg:
#             highest_avg = avg
#             topper = name
    
#     print(f"\n🏆 Topper is {topper} with average {highest_avg:.2f}")

# marking_system(students)



# def find_max_num(arr):
#     max_value = arr[0]
#     for i in arr:
#         if i > max_value:
#             max_value = i
#     return max_value


# print(find_max_num(arr))

# def reverse_array(arr):
#     return arr[::-1]

# print("Reversed array: ", reverse_array(arr))

# def check_sorting(arr):
#     for j in range(len(arr) - 1):
#         if arr[j] > arr[j+1] :
#             return False
#     return True

# print(check_sorting(arr))

# def second_largest(arr):
#     first = second = float('-inf')
#     for i in arr :
#         if i > first:
#             second = first
#             first = i
#         elif i < first and i > second:
#             second = i
#     return second if second != float('-inf') else None

# print(f"Second largest number in given arrays is {second_largest(arr)}")


# def rotate_array(arr, k):
#     k = k % len(arr)
#     return arr[-k:] + arr[:-k]

# print(rotate_array(arr, 2))

arr = [1, 2, 3, 5, 6]
nums = [1, 2, 3, 4, 5, 6]


# def find_missing_num(arr, n):
#     temp_sum = sum(arr)
#     actual_sum = (n * (n + 1)) //2
#     missing_num = actual_sum - temp_sum
#     return missing_num

# print(find_missing_num(arr, 6))

class Solution(object):
    def thirdMax(self, nums):
        first = second = third = float('-inf')
        for i in nums:
            if i > first:
                third = second
                second = first
                first = i
            elif first > i > second :
                third = second
                second = i
            elif first > i and second > i  and i > third :
                third = i
                
        return third if third != float('-inf') else first
print(Solution().thirdMax(nums))