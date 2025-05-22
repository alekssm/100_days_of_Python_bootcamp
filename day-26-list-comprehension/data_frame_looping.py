import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98],
}

students_df = pd.DataFrame(student_dict)
print(students_df)

for index, row in students_df.iterrows():
    print(row.student)