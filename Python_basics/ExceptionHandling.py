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
