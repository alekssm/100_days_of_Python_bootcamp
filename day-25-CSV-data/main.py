# import csv
#
# with open("weather_data.csv") as file:
#     data = list(csv.reader(file))
#
#     for row in data[1:]:
#         print(int(row[1]))

import pandas as pd

weather_data = pd.read_csv("weather_data.csv")
# temperatures = weather_data["temp"].tolist()
# average_temp = sum(temperatures) / len(temperatures)
# print(average_temp)

# print(weather_data["temp"].mean())
# print(weather_data["temp"].max())

# print(weather_data[weather_data.day == "Monday"])
# print(weather_data[weather_data.temp == weather_data.temp.max()])
monday = weather_data[weather_data.day == "Monday"]
temp_C = monday.temp[0] * 9/5 + 32
print(temp_C)



