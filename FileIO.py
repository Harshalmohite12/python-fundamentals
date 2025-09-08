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
