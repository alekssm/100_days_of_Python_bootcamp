list1 = [n*2 for n in range(1,5)]
print(list1)

names = ["Alexis", "Dora", "Jax", "Banderas", "Michael"]

short_names = [name.upper() for name in names if len(name) <= 4]
print(short_names)