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

