"""
ing, cost = {"ingredients": {"water": 50, "coffee": 18,}, "cost": 1.5,}.values()

print(ing)
print(cost)

inserted_coins = [float(input("How many quarters?: ")), float(input("How many dimes?: ")),
                      float(input("How many nickles?: ")), float(input("How many pennies?: "))]

print(inserted_coins)
"""

def take_payment():
    inserted_coins = [input("How many quarters?: "), input("How many dimes?: "),
                      input("How many nickles?: "), input("How many pennies?: ")]
    return inserted_coins

COINS = {
    0: 0.25,
    1: 0.10,
    2: 0.05,
    3: 0.01,
}

print(COINS[0])
coins =take_payment()
print(coins)