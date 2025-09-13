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

    