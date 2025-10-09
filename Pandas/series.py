import pandas as pd

data = [100, 102, 104, 200, 202]

# series = pd.Series(data, index=["A", "B", "C", "E", "F"])
# series.loc["B"] = 10002
# print(series)
# print(series.loc["A"])
# print(series.iloc[1])
# print(series[series < 200])

# calories = {
#     "Day1" : 1700,
#     "Day2" : 2100,
#     "Day3" : 1750
# }

# series = pd.Series(calories)
# print(series)
# print(series[series < 2000])

pokemons = {
    "1" : "Balbasur",
    "2" : "Pikachu"
}

series = pd.Series(pokemons)
print(series)
