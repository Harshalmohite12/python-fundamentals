import matplotlib.pyplot as plt
# import numpy as np

# X = [1, 2, 3, 4]
# Y = [10, 20 , 15 , 25]

# plt.plot(X, Y)
# plt.show()

# x = ["Mon", "Tue", "Wed", "Thu", "Fri"]
# y = [4, 5, 2, 7, 9]

# plt.title("Car sales")
# plt.xlabel("Days of weeks")
# plt.ylabel("No. cars Sold")
# plt.grid()
# plt.plot(x, y,label = "Cars Sold!", color = "purple", linestyle = "--", linewidth = "2", marker = "o")
# plt.legend()
# plt.show() 

# days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
# cars_sold = [3, 0, 4, 6, 2]
# bikes_sold = [10, 12, 7, 3, 9]

# plt.title("Vehicles sales dashboard")
# plt.xlabel("Days of the week")
# plt.ylabel("No. of unit sold")
# plt.grid()

# plt.plot(days, cars_sold, label = "No. of cars sold", color = "Purple", linestyle = "--", linewidth = "2", marker = "o")

# plt.plot(days, bikes_sold, label = "No. of cars sold", color = "green", linestyle = "-.", linewidth = "2", marker = "o")

# plt.legend()
# plt.show()

# days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
# laptops = [5, 7, 6, 8, 4]
# tablets = [3, 4, 5, 6, 2]

# plt.grid()
# plt.title("Tech store sales laptops v/s tablets")
# plt.xlabel("days of week")
# plt.ylabel("no. of unit sold")

# plt.plot(days, tablets, label = "tablet sold", color = "purple", marker = "o", linestyle = "--")
# plt.plot(days, laptops, label = "laptop sold", color = "green", marker = "o", linestyle = "-.")

# plt.legend()
# plt.show()

# ++++++++++++++++++++++++++++++++++++BAR PLOT++++++++++++++++++++++++++++++++++++
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
cars_sold = [3, 2, 4, 6, 8]

plt.bar(days, cars_sold, color="purple", width=0.5, edgecolor="black")
plt.title("Car Sales")
plt.xlabel("Days of the Week")
plt.ylabel("Number of Cars Sold")
plt.show()

# +++++++++++++++++++++++++PIECHART+++++++++++++++++++++++++++++
# regions = ["South", "North" "East" "West"]
# revenue = [1000, 800, 5000, 9000]

# plt.pie(revenue,  colors= ["Green", "yellow", "purple", "red"], autopct="%1.1f%%")
# plt.title("Sales Per Region")
# plt.show()

# ++++++++++++++++++++++++++++++++HISTOGRAM++++++++++++++++++++++++++++++

# scores = [50, 57, 58, 54, 55, 52, 59, 60, 69, 64, 70, 76, 70, 72, 79, 80, 88, 89, 89, 100, 96, 91, 97, 90]

# plt.hist(scores, bins = 5, color="purple", edgecolor = "black")
# plt.xlabel("range of scores")
# plt.ylabel("no. of students fall in the range")
# plt.show()
