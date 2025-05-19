import pandas as pd

#Create DF from a dict /keys are col and values are rows
df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

#Creating Series
ages = pd.Series([13, 19, 21], name="age")

#Read csv file and creates a DF from the data
titanic = pd.read_csv("titanic_data.csv")
print(titanic)

#Creates and writes an Excel file from the data
#titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)

