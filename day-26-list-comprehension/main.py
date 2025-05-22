import random

list1 = [n*2 for n in range(1,5)]
print(list1)

names = ["Alexis", "Dora", "Jax", "Banderas", "Michael"]

short_names = [name.upper() for name in names if len(name) <= 4]
print(short_names)

student_scores = {name: random.randint(2, 7) for name in names}
print(student_scores)

passed_students = {name:score for name, score in student_scores.items() if score > 2}
print(passed_students)