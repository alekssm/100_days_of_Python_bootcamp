travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

fruits = {"apple": 0.40, "orange": 0.35, "banana": 0.25}

"""
for key in travel_log:
    print(key)

for key in travel_log:
    print(travel_log[key])

for item  in travel_log.items():
    print(item)

for key, value in travel_log.items():
    print(key)

for key in travel_log.keys():
    print(key)
"""
""""
for fruit, price in fruits.items():
    fruits[fruit] = round(price * 0.9, 2)

print(fruits)
print("_"*10)

for fruit in fruits.copy():
    if fruits[fruit] == 0.23:
        del fruits[fruit]

print(fruits)
print("_"*10)
"""
"""
menu = {}
for key, value in fruits.items():
    menu[value] = key

print(menu)

menu2 = dict(zip(fruits.values(), fruits.keys()))
print(menu2)
"""


#new_list = [expression for member in iterable if conditional]

sentence = "the rocket came back from mars"

vowels = [char for char in sentence if char in "aeiou"]
print(vowels)

sentence = (
    "The rocket, who was named Ted, came back "
    "from Mars because he missed his friends."
)

def is_consonant(letter):
    vowelss = "aeiou"
    return letter.isalpha() and letter.lower() in vowelss

consonants = [char for char in sentence if is_consonant(char)]
print(consonants)

#new_list = [true_expr if conditional else false_expr for member in iterable]

original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]

new_prices = [price if price > 0 else 0 for price in original_prices]
print(new_prices)

