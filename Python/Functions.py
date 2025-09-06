#create function which return sqaure of number
import math
# def square(num) :
#     num = num ** 2
#     return num

# print(square(5))

# def sum(a, b):
#     return a + b

# print(sum(4, 6))

# def mul(a, b):
#     return a*b

# print(mul(2, " Harshal "))

# def prop(rad):
#     area = 3.14 * rad * rad
#     circumference = 2 * 3.14 * rad
#     return area,circumference

# area, circumference = prop(3)
# print(area, circumference)


# def greet(name = "tony"):
#     return name

# print("Namaste", greet())

# cube = lambda x: x**3
# print(cube(3))

# def even_odd(num) :
#     if(num % 2 == 0) :
#         print("Number is Even")
#     else :
#         print("Number id Odd")
# num = 3

# print(even_odd(num))

# def reverse_string(s):
#     rev = ""
#     for char in s:
#         rev = char + rev   # put current char in front
#     return rev

# print(reverse_string("Harshal"))   # lahSrah

# def max_num(a, b, c):
#     if a >= b and a >= c :
#         return a
#     elif b >= c:
#         return b
#     else: 
#         return c
# result = max_num(2, 5, 9)
# print(result)


# def vowels_count(inp):
#     vowels = 0
#     for char in inp.lower():
#         if char in "aeiou":
#             vowels = vowels + 1
#     return vowels
# result = vowels_count("Harshal")
# print(result)

# def prime_number_checker(num):
#     if num == 0 or num == 1 :
#         return False
#     for i in range (2, num):
#         if num % i == 0:
#             return False
#     return True
    
# if (prime_number_checker(3)) :
#     print("It is A prime number")
# else :
#     print("It is not a prime number")   


# strr = "Nayan"
# def palindromecheckerr(strr):
#     strrr = ""
#     for char in strr :
#         strrr = char + strrr
#     if strr.lower() == strrr.lower() :
#         return True
#     else:
#         return False

# if palindromecheckerr(strr) :
#     print("It is a PALINDROME")
# else :
#     print("It is not a PALINDROME")

# def second_largest_num_checker(num) :
#     temp = 0
#     j = 0
#     for i in num :
#         if i > temp :
#             j = temp
#             temp = i
#         elif i > j and i !=temp :
#             j = i
#     return j

# num = [2, 3, 0, 13, 453, 21, 421]
# print(second_largest_num_checker(num))


# x = 99
# def chaicoder(num):
#     def actual(x):
#         return x**num
#     return actual

# f = chaicoder(2)
# g = chaicoder(3)

# print(f(3))
# print(g(3))
            
# str1 = "My name is harshl lalaso mohite. Hello, I am"
# li = []
# for i in str1.split(" "):
#     li.append(i)
# print(len(li))
