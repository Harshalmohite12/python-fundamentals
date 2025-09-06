# class Student:
#     name = "Harshal Mohite"
    
# s1 = Student()
# print(s1.name)

# class Student:
    
#     def __init__(self, name, marks1, marks2, marks3):
#         self.name = name
#         self.marks1 = marks1
#         self.marks2 = marks2
#         self.marks3 = marks3
#         print("Addong new student...")
        
#     def average(self):
#         return (self.marks1 + self.marks2 + self.marks3)/3

# s1 = Student("Harshal", 90, 90, 90)
# print("Avergae marks of student",s1.name,"is",s1.average(),"%")


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
# acc.withdraw(400)    # ❌ Not allowed (would go to -600)
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


