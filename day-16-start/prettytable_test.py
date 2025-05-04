from prettytable import PrettyTable

pokemons = ["Pikachu", "Squirtle", "Charmander"]
types = ["Electric", "Water", "Fire"]

table = PrettyTable(title="Great table")

table.field_names = ["Pokemon Name", "Type"]
for i in range(3):
    table.add_row([pokemons[i], types[i]])

print(table)