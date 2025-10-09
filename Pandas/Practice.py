import pandas as pd
import numpy as np

students_data = {
    "Name" : ["Harshal", "Shweta", "Chaitanya", "Vighnesh", "Saloni"],
    "Age" : [21, 20, 22, 21, 20],
    "Marks" : [99, 95, 100, 45, 76]
}

df = pd.DataFrame(students_data)

df["Result"] = np.where(df["Marks"] > 50, "Pass", "Fail")
# print(df)

# print(df.iloc[1])
# print(df.loc[3])

new_student = pd.DataFrame([{"Name" : "Rahul",
                             "Age" : 23,
                             "Marks" : 70}])

# df = pd.concat([df, new_student], ignore_index=True)
# print(df)