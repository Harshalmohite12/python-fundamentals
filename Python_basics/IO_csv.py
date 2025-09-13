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