import pandas as pd

#Primary Fur Color - column with squirrel color

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250517.csv")

#Checks what squirrel colors there are in the data / filters the rows where the information is missing
squirrel_colors = set(color for color in data["Primary Fur Color"] if isinstance(color, str))

squirrel_color_data = {
    "Fur Color": [],
    "Count": [],
}

#Finds how many of each color there are and adds it to the dictionary
for col in squirrel_colors:
    col_count = len(data[data["Primary Fur Color"] == col])
    squirrel_color_data["Fur Color"].append(col)
    squirrel_color_data["Count"].append(col_count)

print(squirrel_color_data)

sq_data = pd.DataFrame(squirrel_color_data)
sq_data.to_csv("squirrel_data.csv")
