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
