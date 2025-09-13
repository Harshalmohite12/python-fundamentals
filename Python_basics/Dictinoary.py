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