import pandas as pd

# data = {
#     "Name" : ["Harshal", "Shweta", "Chaitanya"],
#     "Age" : [21, 20, 22]
# }

# df = pd.DataFrame(data)
# print(df)
# print(df.loc[0])
# print(df.iloc[1])

# df["Job"] = ["Enginner", "Desginer", "Gamer"]
# # print(df)

# new_row = pd.DataFrame([{"Name" : "Vighnesh", "Age" : 19, "Job" : "JCB"}])
# df = pd.concat([df, new_row])
# print(df)

# df = pd.read_csv("Pandas/pokemons.csv")
# print(df.to_string())
# print(df["Name"])
# print(df["Total"])
# print(df["HP"])
# print(df[["Name", "Type 1", "Type 2"]].to_string())

# df = pd.read_csv("Pandas/pokemons.csv", index_col="Name")
# print(df) 
# print(df.loc["Charizard"])
# print(df.loc["Charizard", ["Type 1", "Type 2"]])
# print(df.loc["Charizard":"Pikachu", ["No", "Type 1", "Type 2"]])
# print(df.iloc[0])
# print(df.iloc[0:11:2])
# print(df.iloc[0:11:2, 0:3])

# pokeomon = input("Enter Pokemon Name: ")

# try:
#     print(df.loc[pokeomon])
# except KeyError:
#     print(f"{pokeomon} not found")

# print(df[df["HP"] > 50].to_string())
# print(df[df["Legendary"] == True].to_string())


# ++++++++++++++++++++++++++++++++++FILERING++++++++++++++++++++++++++

# water_pokemons = df[(df["Type 1"] == "Water") | (df["Type 2"] == "Water")]
# ff= df[(df["Type 1"] == "Fire") & (df["Type 2"] == "Flying")]
# EE = df[(df["Type 1"] == "Electric") & (df["Type 2"] == "Flying")]

# print(ff)
# print(EE)
# print(water_pokemons.to_string())

# ++++++++++++++++++++++++++++++++++++Aggregate Function++++++++++++++++++++++++++++++++
df = pd.read_csv("Pandas/pokemons.csv")

#Aggregate function for full datasset
# print(df.mean(numeric_only=True))
# print(df.sum(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))
# print(df.count(numeric_only=True))
# print(df.count())

#Aggregate function for single column
# print(df["Speed"].mean())
# print(df["Speed"].sum())
# print(df["Speed"].min())
# print(df["Speed"].max())
# print(df["Speed"].count())

# group = df.groupby("Type 1")
# print(group["Speed"].mean())
# print(group["Speed"].sum())
# print(group["Speed"].min())
# print(group["Speed"].max())
# print(group["Speed"].count())

# +++++++++++++++++++++++++++Data Cleaning++++++++++++++++++++++

#Dropping irrelevant coloumns
# df = df.drop(columns=["No", "Generation", "Legendary"])

#Handling missing data
# df = df.dropna(subset=["Type 2"])
# df = df.fillna({"Type 2" : "None"})

#Fix inconsistent value
# df["Type 1"] = df["Type 1"].replace({"Grass" : "GRASS", "Fire" : "FIRE", "Water" : "WATER"})

#Standardised text
# df["Type 1"] = df["Type 1"].str.lower()

#Fix data types
# df["Legendary"] = df["Legendary"].astype(int)

#Fix Duplicate Values
# df = df.drop_duplicates()
# print(df)


# data = {
#     "Name": ["Harshal", "Shweta", "Chaitanya", "Vighnesh", "Saloni"],
#     "Age": [21, 20, 22, 21, 20],
#     "Marks": [99, 95, 100, 45, 76]
# }

# df = pd.DataFrame(data)
# print("Original DataFrame:\n", df)

# # Set "Name" as the index
# df_indexed = df.set_index("Name")
# print("\nAfter setting 'Name' as index:\n", df_indexed)

# # Reset the index back to default
# df_reset = df_indexed.reset_index()
# print("\nAfter resetting index:\n", df_reset)

# multi_df = df.set_index(["Age", "Marks"])
# print("\nMultiIndex DataFrame:\n", multi_df)
