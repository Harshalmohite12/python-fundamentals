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
