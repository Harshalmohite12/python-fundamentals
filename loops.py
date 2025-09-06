# numbers = [1, 3, 4, 2,-3, 2, -2, -3, -8, 9, -5]
# pos_num_count = 0

# for num in numbers :
#     if num > 0 :
#         pos_num_count += 1
# print(pos_num_count)


# n = int(input("Enter a number: "))
# total_sum = 0

# for i in range(1, n+1) :
#     if(i % 2 == 0) :
#         total_sum = total_sum + i
# print(total_sum)

# n = int(input("Enter number: "))

# for i in range (1, 11) :
#     if i == 5:
#         continue
#     print(n ,"x", i ,"=", n*i)

# str = str(input("Enter a string: "))
# rev = ""

# for cha in str :
#     rev = cha + rev
# print(rev)

# str = str(input("Enter s string: "))

# for char in str :
#     if str.count(char) == 1 :
#         print("found it, the first non repeated character : ", char)
#         break

# n = int(input("Enter a number: "))
# fact = 1

# for i in range (1, n+1) :
#     fact *= i
# print(fact)

# while n > 0 :
#     fact *= n
#     n -= 1  
# print("number: ", fact)

# while True:
#     n = int(input("Enter a number: "))
#     if  0 <  n <= 11:
#         break

# n = int(input("Enter a number: "))
# is_prime = True

# if n <= 1 :
#     print("Not a prime number")
# else :
#     for i in range (2, n) :
#         if n % i == 0 :
#             is_prime = False
#             break
# if is_prime:
#     print(n, "is prime number")
# else :
#     print("not a prime number")

# fruits = ["apple", "banana", "mango", "orange", "grapes", "apple", "banana"]

# seen = set()
# duplicates = set()

# for fruit in fruits:
#     if fruit in seen:
#         duplicates.add(fruit)
#     else:
#         seen.add(fruit)
# print("Duplicate items are:", list(duplicates))


# fruits = ["apple", "banana", "mango", "orange", "grapes", "apple"]

# duplicates = []

# for fruit in fruits:
#     if fruits.count(fruit) > 1 and fruit not in duplicates:
#         duplicates.append(fruit)

# print("Duplicate items are:", duplicates)

#BEHIND THE SCENES OF LOOPS:

