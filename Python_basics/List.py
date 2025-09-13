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
print(SuperHeroes_copy)
print(SuperHeroes)

# SuperHeroes[4] = "SuperMan"
# print(SuperHeroes)

# for heroes in SuperHeroes:
#     print(heroes, end=" ")

# if "AntMan" in SuperHeroes :
#     print("Yes! it is present")

# size=11
# squared_num = [x**2 for x in range(size)]
# print(squared_num)

