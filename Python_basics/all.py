print("Hello World");
# print('chai ' + 'code');
# print(2**10000) 
#STRINGS ARE IMUTABLE

str = "Tony Stark";
str1 = str[0]; #str1 stores first character of string str. which T.
# print(str1);
str2 = str[0:5]; #str2 slice Tony from str and store it into str2. This is called Slicing.
# print(str2);

num_list = "0123456789"
# print(num_list[:])
# print(num_list[:7])
# print(num_list[3:])
# print(num_list[0:7:3])
# print(num_list[-1:])

#methods of Strings
# print(str.upper())
# print(str.lower())
# print(str.strip()) #remmove unwated spaces.
# print(str.replace("Tony", "Doom"))
# print(str.find("Stark")) #it will return the index of the word(First lettter) that you want to find in string.
# print(str.count("Tony")) #it return count that how many times it appears in string.
# print(len(str))
# print("Stark" in str) #it check the given string is present in your string as it is.

#how to convert string ino list & list into string
str0 = "Doom, Tony, Rid, Steve"
# print(str0.split(", "))

str00 =["Doom", "Tony", "Rid", "Steve"]
# print("".join(str00[0]))
# print(", ".join(str00))

# chai_type = "Masala"
# quantity = 2
# order = "i want to order {} cup of {} chai"
# print(order.format(quantity, chai_type))


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Practiice of strings
name = "IronManTony"      
# print(name[0:4]);
#STRINGS ARE MUTABLE

SuperHeroes = ["IronMan", "BatMan", "SpiderMan", "AntMan", "Hulk"];
# print(SuperHeroes);

# print(SuperHeroes[0:3]) #slicing same as string.
# SuperHeroes.append("Captain") # add value at last of list.
# SuperHeroes.pop() #removes last character.
# SuperHeroes.remove("BatMan") # remove the given thing
# SuperHeroes.insert(1, "Doom") #inserting into liost with specefic position
SuperHeroes_copy = SuperHeroes.copy() #it gives copy of the list. in memory it creates copy instead of pointing towards the same reffrence.
SuperHeroes_copy.append("Doom") # now it will add "Doom" to copy variable and do not chamge orignal variable.
# print(SuperHeroes_copy)
# print(SuperHeroes)

# SuperHeroes[4] = "SuperMan"
# print(SuperHeroes)

# for heroes in SuperHeroes:
#     print(heroes, end=" ")

# if "AntMan" in SuperHeroes :
#     print("Yes! it is present")

# size=11
# squared_num = [x**2 for x in range(size)]
# print(squared_num)

#TUPLES ARE IMMUTABLE.

SuperHeroes = ("IronMan", "BatMan", "SpiderMan", "AntMan", "Hulk")
DC_SuperHeroes = ("SuperMan", "Flash", "AquaMan")
All_Heroes = SuperHeroes + DC_SuperHeroes
# print(All_Heroes)
# print(SuperHeroes)

# if "SuperMan" in DC_SuperHeroes :
#     print("yessssssss")
# else:
#     print("noooooooooo")

# print(SuperHeroes.count("BatMan"))

(RDJ, Robert, Tom, Paul, Mark) = SuperHeroes #Wrapping UnWrapping
# print(RDJ)
# print(type(SuperHeroes))
# sup_heroes_types = {"Hero" : "IronMan", 
#                     "Patriot" : "Captain", 
#                     "AntiHero" : "Loki"
#                     }
# print(sup_heroes_types["Hero"]) #if you enterd wrong key it will throw error

# print(sup_heroes_types.get("Patriot")) #it will not throe error. it will print none.

# sup_heroes_types["AntiHero"] = "Deadpool"

# sup_heroes_types["Green"] = "Hulk"

# print(len(sup_heroes_types))

# sup_heroes_types.pop("Green") #it will print or return value of green(if you print this) and remove key value pair of green.

# sup_heroes_types.popitem(); #it removes last items. 

# del sup_heroes_types["Green"] #delete specefic item.

# sup_heroes_types_copy = sup_heroes_types.copy()

# print(sup_heroes_types)

# for sup in sup_heroes_types:
#     print(sup)
    
# for sup in sup_heroes_types:
#     print(sup, sup_heroes_types[sup])
    
# for key, value in sup_heroes_types.items():
#     print(key, value)

# if "Hero" in sup_heroes_types:
#     print("Yessssssssss")
    
SuperHero_Shop = {
    "SpiderMan" : {"Andrew" : "The Amazing Spider Man", "Tom" : "MCU Spider Man"},
    "IronMan" : {"Tony" : "OG IronMan", "Tom" : "Supereme IronMan"}
}

# print(SuperHero_Shop)
# print(SuperHero_Shop["SpiderMan"])
# print(SuperHero_Shop["SpiderMan"]["Andrew"])

# squared_nums = {x:x**2 for x in range(6)}
# print(squared_nums)
# squared_nums.clear()
# print(squared_nums)

# keys = ["harshal", "harshal1", "harshal2"]
# deafult = "smart"
# new_dict = dict.fromkeys(keys, deafult)
# print(new_dict)

# SuperHero_Shop.update( {"Antman" : {"Tony" : "OG IronMan", "Tom" : "Supereme IronMan"}})
# print(SuperHero_Shop["Antman"])


# userScore = int(input("Give me score: "))
# print(userScore+1234)

# age = int(input("Enter age: "));

# if age < 13 :
#     print("Minor")
# elif age >= 13 and age < 18 :
#     print("Still Minor")
# elif age >= 18 and age < 60 :
#     print("Adult")
# elif age >= 60 and age < 100 :
#     print("super senior")
# else :
#     print("why are you not dead yet!")
    
    
#Q2:- movie tickets are priced based on the age 12dollars for the adults and 8 dollars for children. Enveryone gets discount of 2rs on wednesday.

# age = int(input("Enter Your Age: "))
# day = str(input("Enter todays Day: ")).lower()

# if age < 13 :
#     if day == "wednesday" :
#         TicketPrice = 6
#     else :
#         TicketPrice = 8
# else :
#     if day == "wednesday" :
#         TicketPrice = 10
#     else :
#         TicketPrice = 12

# print("You tickets price is", TicketPrice , "dollars")

# age =11
# day = "wednesday"
# price = 12 if age >= 18 else 8
# print(price);


#ASSIGN A LETEER GRADE BASED ON THE PROGRESS: A(90-100), B(80-89), C(70-79), D(60-69), F(BELOW 60) 

# marks = int(input("Enter marks: "))
# if marks>=90 and marks<=100:
#     print("Grade A")
# elif marks>=80 and marks<=89:
#     print("Grade B")
# elif marks>=70 and marks<=79:
#     print("Grade C")
# else:
#     print("Fail")

#Write a program that checks whether a given year is a leap year.
# given_year = int(input("Enter Year: "))
# if (given_year % 400==0) or (given_year % 4 == 0 and given_year % 100 != 0):
#     print(given_year, "is a leap year")
# else:
#     print(given_year, "is not leap year")


#Write a program that takes three numbers and prints the largest one.
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter number number: "))

# if (a > b and a > c) :
#     print("Biggest number:",a)
# elif (b > c):
#     print("Biggest number:",b)
# else:
#     print("Biggest number:",c)
    

#atm
# ac_balance = int(input("Enter Account Balance: "))
# wi_money = int(input("How much you want withdraw: "))
# if ac_balance < wi_money :
#     print("Insufficient Balance ")
# elif ac_balance >= wi_money :
#     cash = ac_balance - wi_money
#     print("This is remaning Balance",cash)

#Question: “Body Mass Index (BMI) Calculator with Category”
# weight = float(input("Enter weight in KG: "))
# height = float(input("Enter height in meters: "))
# bmi = weight / (height*height)

# if bmi < 18.5:
#     print("underweight")
# elif bmi >= 18.5 and bmi < 24.9 :
#     print("normal weight")
# elif bmi >=25 and bmi <29.9 :
#     print("overweight")
# elif bmi >= 30 :
#     print("obese")
    
#Question: “Advanced Loan Eligibility Checker”
# age = int(input("Enter age: "))
# mon_income = int(input("Enter Your monthly income: "))
# existing_loan = int(input("Enter Your Existing Loan: "))
# credit_score = int(input("Enter your credit score (300-900): "))
# emp_type = input("Enter Employment Type (Salaried/SelfEmployed): ").lower()

# DTI = (existing_loan / mon_income) * 100
# reasons = []

# # Age check
# if not (21 <= age <= 60):
#     reasons.append("Age not in range (21-60)")

# # DTI check
# if DTI > 40:
#     reasons.append("DTI too high")

# # Credit score check
# if credit_score < 650:
#     reasons.append("Credit score too low")

# # Employment type check
# if emp_type == "selfemployed" and mon_income < 50000:
#     reasons.append("Income too low for self-employed")

# # Final decision
# if reasons:
#     print("Loan Rejected:")
#     for r in reasons:
#         print("-", r)
# else:
#     print("Loan Approved")

# print(type(reasons))


###########################################################################
# dist = float(input("Enter How much distance you want travel(KM): "))

# if dist <= 0 :
#     print("invalid distance")
# elif dist < 3 :
#     print("Go by WALK")
# elif dist < 15 :
#     print("Get a BIKE")
# elif dist >= 15 :
#     print("Get a Car")

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

# class Student:
    
#     def __init__(self, name, marks1, marks2, marks3):
#         self.name = name
#         self.marks1 = marks1
#         self.marks2 = marks2
#         self.marks3 = marks3
#         print("Adding new student...")
        
#     def average(self):
#         return (self.marks1 + self.marks2 + self.marks3)/3


# # Now create the student object AFTER class definition
# s1 = Student("Harshal Mohite", 90, 90, 90)
# print("Student name:", s1.name)
# print("Average marks of student", s1.name, "is", s1.average(), "%")


# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
    
#     def full_name(self):
#         return f"{self.brand} {self.model}"
    
#     def fuel_type(self): #POLYMORPHISM
#         return "Petrol OR Disel"
    
#     @staticmethod
#     def static_method(): #this is static method
#         return "This is static method"
    
# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.__battery_size = battery_size  # here we make battery_size variable private using __ at the start.
        
#     def get_batttery_size(self):  #this is get method.
#         return self.__battery_size
    
#     def fuel_type(self): #POLYMORPHISM
#         return "Electric Charge"

# mytesla = ElectricCar("Tesla", "S1", "81Kwh")
# print(mytesla.battery_size) # now this will not work because battery_size variable is private we can not directly acces it we have to acees it through get method

# print(mytesla.full_name())
# print(mytesla.get_batttery_size())
# print(mytesla.fuel_type())

# mysafari = Car("tata", "safari")
# print(mysafari.fuel_type())

# print(Car.static_method()) #this is way of calling static method.




# class BankAccount:
#     def __init__(self, account_number, balance = 0):
#         self.account_number = account_number
#         self.balance = balance
        
#     def deposit(self, amount):
#         self.balance = amount + self.balance
#         return self.balance 
    
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("INSUFFICIENT BALANCE")
#             return self.balance
#         self.balance = self.balance - amount
#         return self.balance
    
#     def check_balance(self):
#         return self.balance
    
# customer1 = BankAccount("H1U768", 1000)
# customer1.deposit(8000)
# print(customer1.check_balance())

# class SavingsAccount(BankAccount):
#     def add_interest(self, rate):
#         intrest = self.balance * (rate/100)
#         self.balance += intrest
#         print("Intrest added", intrest , "Total Balance: ",self.balance)
        
# customer2 = SavingsAccount("H2U123", 1000)
# customer2.deposit(500)          # balance = 1500
# customer2.add_interest(10)      # adds 10% of 1500 = 150
# print(customer2.check_balance())

# class CurrentAccount(BankAccount):
#     def __init__(self, account_number, balance = 0, overdraft_limit = 0):
#         super().__init__(account_number, balance)
#         self.overdraft_limit = overdraft_limit
    
#     def withdraw(self, amount):
#         if amount > self.overdraft_limit + self.balance:
#             print("INSUFFICIENT BALANCE")
#             return self.balance
#         else:
#             self.balance = self.balance - amount
#             print("Your current balnce is", self.balance, "withdraw amount: ",amount)
#             return self.balance
    
        
# acc = CurrentAccount("C123", 1000, overdraft_limit=500)

# acc.withdraw(1200)   # Allowed → balance = -200
# acc.withdraw(400)    # Not allowed (would go to -600)
# acc.withdraw(200)    # Allowed → balance = -400


# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
        
#     def average(self):
#         totalmarks = 0
#         for i in self.marks:
#             totalmarks += i
#         return totalmarks/len(self.marks)
            
#     def grade(self):
#         if self.average() >= 90:
#             return "Grade A"
#         elif self.average() >= 80:
#             return "Grade B"
#         elif self.average() >= 70:
#             return "Grade C"
#         else:
#             return "Fail"
    
#     @classmethod
#     def topper(cls, students):
#         top_student = students[0]  # assume first student is topper initially
#         for student in students:
#             if student.average() > top_student.average():
#                 top_student = student
#         return top_student
    
    
# s1 = Student("Harshal", [95, 90, 92])   # avg ~ 92.3 (A)
# s2 = Student("Amit", [85, 82, 80])      # avg ~ 82.3 (B)
# s3 = Student("Riya", [71, 74, 70])      # avg ~ 71.7 (C)
# s4 = Student("Kiran", [60, 55, 65])     # avg ~ 60 (Fail)

# students = [s1, s2, s3, s4]

# print(s1.name, s1.average(), s1.grade())
# print(s2.name, s2.average(), s2.grade())
# print(s3.name, s3.average(), s3.grade())
# print(s4.name, s4.average(), s4.grade())

# topper = Student.topper(students)
# print("Topper is:", topper.name, "with average", topper.average(), "and grade", topper.grade())


# def main(func):
#     def wrapper(*args, **kwargs):
#         print("Hello")
#         return func(*args, **kwargs)
#     return wrapper

# @main
# def add(a, b):
#     print(a+b)
    

# add(4 ,67)


# def log(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling {func.__name__} with {args} {kwargs}")
#         return func(*args, **kwargs)
#     return wrapper

# @log
# def multiply(a, b):
#     return a * b

# print(multiply(3, 4))

# def decorator(func):
#     count =0
#     def wrapper():
#         nonlocal count
#         func()
#         count += 1
#         print(f"This functon {func.__name__} is called {count} times.")
#     return wrapper

# @decorator
# def say_hello():
#     print("Hello Wolrd!")
    
# say_hello()
# say_hello()
# say_hello()
# say_hello()


# x = 100   # global

# def outer():
#     count = 0   # enclosing (outer function variable)

#     def middle():
#         nonlocal count   # refers to 'count' in outer()
#         count += 1
#         print("Middle:", count)

#         def inner():
#             nonlocal count   # still refers to 'count' in outer()
#             count += 1
#             print("Inner:", count)

#         inner()

#     middle()
#     print("Outer:", count)

# outer()


# def show_name(func):
#     def wrapper(*args):
#         print(f"Calling function: {func.__name__}")
#         return func(*args)
#     return wrapper



# @show_name
# def add(a, b):
#     return a + b

# @show_name
# def greet(name):
#     print(f"Hello {name}!")
    
# print(add(3, 5))
# greet("Harshal")

# def safe_divide(func):
#     def wrapper(*args, **kwargs):
#         a = [*args]
#         for i in range (0, len(a)):
#             if a[i] == 0:
#                 return "Cannot divide by zero"
#         return func(*args, **kwargs)
#     return wrapper

# @safe_divide
# def divide(a, b):
#     ressult =  a / b
#     return ressult

# print(divide(10, 2))
# print(divide(5, 0))


# try:
#     a = int(input("Enter a number: "))
#     for i in range (1, 11):
#         print(f"{a} X {i} = {a*i}")
# except Exception as e:
#     print("INVALID ERROR")


# print("Some important lines of code")
# print("End of code")

# try:
#     a = int(input("Enter index: "))
#     b = [3, 4, 43]
#     print(b[a])
# except ValueError:
#     print("Enter inddex as number")
# except IndexError:
#     print(f"Inavlid index. indes lies between 0 to {len(b)-1}")
# except :
#     print("What is this input!")


# def func():
#     try:
#         a = int(input("Enter index: "))
#         b = [3, 4, 43]
#         print(b[a])
#     except:
#         print("INVALID")
#     finally:
#         print("It will execute everytime")
# func()

# age = int(input("Enter your age: "))
# if(age < 1):
#     raise ValueError("Age can not less than zero")

# try:
#     age = int(input("Enter your age: "))
#     if(age < 1):
#         raise ValueError("Age can not less than zero")
#     print(f"your age is {age}")
# except ValueError as e:
#     print(e)

# class InvalidAgeError(Exception):
#     pass
# try:
#     age = int(input("Enter your age: "))
#     if(age < 1):
#         raise InvalidAgeError("Age can not less than zero")
#     print(f"your age is {age}")
# except InvalidAgeError as e:
#     print(f"Your age is : {e}")

# class InsufficientBalanceError(Exception):
#     pass

# class BankAccount():
#         def __init__(self, account_number, balance=0):
#             self.account_number = account_number
#             self.balance = balance
#         def deposit(self, amount):
#             self.balance = self.balance + amount
#             return self.balance
#         def withdraw(self, amount):
#             if amount > self.balance:
#                 raise InsufficientBalanceError("Not enough balance")
#             self.balance = self.balance - amount
#             return self.balance
    
# a = BankAccount("HADFSDH", 1000)
# try:
#     print(a.withdraw(1100))
# except InsufficientBalanceError as e:
#     print(f"Error: {e}")

# f = open("OOP.py", "r", encoding="utf-8")  # <-- FIX
# data = f.read()
# print(data)
# f.close()

# f = open("Demo.txt", "w")
# data = f.write("HEllo my name is demo")
# print(data)
# f.close()

# with open("First.py", "r+") as h: #by using with it automatically closes the file.
#     data = h.read()
#     print(data)                   # No need of h.close()
    
# with open("demo.txt", "w")as h:
#     h.write("Hello my name is harshal \n")
#     h.write("Hello my surname is mohite \n")

# with open("demo.txt", "r") as h:
    # data = h.read()
    # print(data)
    # for line in h:
        # print(line.strip())
    # line1 = h.readline()
    # line2 = h.readline()
    # print("First line:", line1.strip())
    # print("Second line:", line2.strip())
    # h.seek(0) #it resets your pointer at 0.
    # data = h.readlines()
    # print(data)
    # print(h.seek(h.tell())) #it tells now where is pointer
    
# overwrite mode
# with open("demo.txt", "w") as f:
#     f.write("This is a fresh file\n")

# # append mode
# with open("demo.txt", "a") as f:
#     f.write("Adding one more line\n")

# # read after append
# with open("demo.txt", "r") as f:
#     print(f.read())

# with open("log.txt", "w") as f:
#     f.write("First experiment: Accuracy = 85%\nSecond experiment: Accuracy = 87%\n")
    
# with open("log.txt", "a") as f:
#     f.write("Third experiment: Accuracy = 90%")

# with open("log.txt", "r") as f:
#     for line in f:
#         print(line.strip())

#finding a word in file.
# with open("demo.txt", "r") as f:
#     for line in f:
#         if "Harshal" in line:
#             print("Found:", line.strip())
            

#Updating content in a file (replace word):
# Read original file
# with open("demo.txt", "r") as f:
#     content = f.read()

# # Replace a word
# content = content.replace("Harshal", "Harsh")

# # Write back to the file
# with open("demo.txt", "w") as f:
#     f.write(content)
#     print(content)

# with open("demo.txt", "r") as file:
#     for line in file:
#         print(line.strip())
    
# find = "Harsh"
# with open("demo.txt", "r") as file:
#     for line in file:
#         if find in line:
#             print("Found: ",line)

# with open("demo.txt", "r") as file:
#     content = file.read()
    
# content = content.replace("Harsh", "Harshal")

# with open("demo.txt", "w") as file:
#     file.write(content)
#     print(content)
    
# with open("demo.txt", "a") as file:
#     file.write("\n this is new line addded by appending mode")

import csv

# with open("students.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# student_count = 0
# with open("students.csv", "r") as file:
#     read = csv.reader(file)
#     header = next(read)
#     print("Header is : ", header)
#     for row in read:
#         print(row)
        # student_count += 1
    # print(student_count)
    
# with open("students.csv", "w", newline = "") as file:
#     write = csv.writer(file)
#     write.writerow(["Name", "Math", "Science", "English"])
    
#     write.writerow(["Harshal", "89", "86", "98"])
#     write.writerow(["Shweta", "89", "86", "98"])
#     write.writerow(["Chaitanya", "89", "86", "98"])
    


# rows = [
#     ["Name", "Math", "Science", "English"],
#     ["Harshal", 90, 85, 92],
#     ["Anita", 78, 88, 80],
#     ["Rohit", 85, 80, 90]
# ]

# with open("students.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(rows)   # writes all rows in one go


# with open("books.csv", "w", newline="") as file:
#     writer = csv.writer(file)
    
#     writer.writerow(["Title", "Author", "Year"])

#     writer.writerow(["Physics", "H.C. VERMA", "2005"])
#     writer.writerow(["Chemistry", "Pankaj Sir PW", "2008"])
#     writer.writerow(["Maths", "Alakh Sir", "2012"])

# rows = [
#     ["name", "director", "rating"],
#     ["Singham", "rohit shetty","4.5"],
#     ["Singham2", "rohit shetty", "4.8"],
#     ["Singham3", "Rohit Shetty", "9.8"]
# ]

# with open("movies.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(rows)
    
# with open("movies.csv", "a", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Singham4", "rohit shetty", "8.8"])

# data = [
#     ["Players", "Team", "Runs"],
#     ["Virat", "RCB", "973"],
#     ["Rohit", "MI", "865"],
#     ["Shubhman", "GT", "890"]
# ]
# with open("players.csv", "w", newline="") as file:
#     writer = csv.writer(file)
    
#     writer.writerows(data)
    
# with open("players.csv", "r") as file:
#     reader = csv.reader(file)
#     next(reader)
#     for read in (reader):
#         print(read[0])
    
# with open("players.csv", "a", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["gamhir", "KKR", "780"])
    
# with open("players.csv", "r") as file:
#     reader = csv.reader(file)
#     next(reader)
#     for read in (reader):
#         print(read[0],"->",read[2])
        
# total_runs = 0
# with open("players.csv", "r") as file:
#     reader = csv.reader(file)
#     next(reader)
#     for read in (reader):
#         runs = int(read[2])
#         total_runs += runs
#     print(total_runs)


# with open("players.csv", "r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row["Players"], "->", row["Team"], "->", row["Runs"])

# fieldnames = ["Players", "Team", "Runs"]

# with open("players.csv", "w", newline="") as file:
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
    
#     writer.writeheader()
    
#     writer.writerow({"Players" : "Virat", "Team" : "RCB", "Runs" : "973"})
#     writer.writerow({"Players" : "rohit", "Team" : "MI", "Runs" : "700"})
#     writer.writerow({"Players" : "gautam", "Team" : "KKR", "Runs" : "890"})

# Fieldnames = ["ID", "name", "department", "salary"]

# with open("employees.csv", "w", newline="") as file:
#     writer = csv.DictWriter(file, fieldnames=Fieldnames)
    
#     writer.writeheader()
    
#     writer.writerow({"ID" : "01", "name" : "harshal", "department" : "HR", "salary" : "10000000"})
#     writer.writerow({"ID" : "02", "name" : "shweta", "department" : "MANAGER", "salary" : "2000000000"})
#     writer.writerow({"ID" : "03", "name" : "chaitanya", "department" : "SDE", "salary" : "999999999999"})
    
# with open("employees.csv", "r") as file:
#     reader = csv.DictReader(file)
    
#     for row in reader:
#         print(row["name"])
        
# with open("employees.csv", "r") as file:
#     reader = csv.DictReader(file)
    
#     for row in reader:
#         print(row["name"], "->", row["salary"])
        
# with open("employees.csv", "a", newline="") as file:
#     writer = csv.DictWriter(file, fieldnames=Fieldnames)
    
#     writer.writerow({"ID" : "04", "name" : "sujit", "department" : "Mechanical", "salary" : "97213132871253"})
    
# with open("employees.csv", "r") as file:
#     reader = csv.DictReader(file)
    
#     for row in reader:
#         print(row)
  
# total_salary = 0      
# with open("employees.csv", "r") as file:
#     reader = csv.DictReader(file)
    
#     for row in reader:
#         total_salary += int(row["salary"])
# print("Total Salary: ",total_salary)

import json

# data = {
#     "name" : "Harshal",
#     "age" : 21,
#     "skills" : ["python", "java", "numpy"],
#     "isStudent" : True
# }

# with open("dataa.json", "w") as file:
#     json.dump(data, file, indent=4)
    
# with open("dataa.json", "r")as file:
#     my_data = json.load(file)
    
#     print(my_data)
#     print(my_data["name"])
#     print(my_data["age"])
#     print(my_data["skills"])

# with open("student.json", "r") as file:
#     data_files = json.load(file)
    
# data_files.update({"name": "Shweta", "age": 22})

# with open("student.json", "w") as file:
#     json.dump(data_files,file,indent=4)



# with open("student.json", "r") as file:
#     data = json.load(file)
    
# data["students"].append({"name": "Shweta", "age": 20})

# with open("student.json", "w") as file:
#     json.dump(data, file, indent=4)

#EXAMPLE OF PYTHON -> JSON STRING [json.dumps]:
# import json

# data = {
#     "name": "Harshal",
#     "age": 21,
#     "skills": ["python", "java"],
#     "isStudent": True
# }

# Convert dict → JSON string
# json_string = json.dumps(data, indent=4)
# print(type(json_string))   # <class 'str'>
# print(json_string)


#EXAMPLE OF JSON STRING -> PYTHON DICT [json.loads]:
# import json

# json_string = '{"name": "Shweta", "age": 22, "skills": ["C++", "ML"]}'

# Convert JSON string → Python dict
# python_data = json.loads(json_string)
# print(type(python_data))   # <class 'dict'>
# print(python_data["name"]) # Shweta

    
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