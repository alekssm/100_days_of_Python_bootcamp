import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

lucky_winner = friends[random.randint(0,len(friends) - 1)]

print(lucky_winner)