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

#Creates and writes an Excel file from the data
#titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)

#Selects a specific column from the DF / returns a Series
age = titanic.Age

survived = titanic["Survived"]

#Selects more than one column from DF / returns a DF
age_and_sex = titanic[["Age", "Sex"]]

#Selects and returns only thr rows where the condition is True / In the example is the value in column "Age" > 35
above_35 = titanic[titanic.Age > 35]

searched_classes = [2, 3]
#Selects and returns only the rows where the condition is True / isin([]) - is the value of the column in the provided list
class_2_3 = titanic[titanic.Pclass.isin(searched_classes)]

#Selects and returns only the rows where the condition is not Null / notna()
known_class = titanic[titanic.Pclass.notna()]

#Selects and returns only the column of the passengers who are above 35
above_35_names = titanic.loc[titanic.Age > 35, "Name"]

#Select and returns only the columns chosen based on index in the FD
ten_to_25 = titanic.iloc[9:24, 4:6]
print(ten_to_25)

#It will assign the value to the chosen rows and columns cells
#titanic.iloc[0:3, 1:5] = "koza"
