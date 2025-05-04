from menu import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

COINS = {
    0: 0.25,
    1: 0.10,
    2: 0.05,
    3: 0.01,
}

money = 0

def report():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}mg")
    print(f"Money: ${money}")

def take_order():
    order = input("What would you like? (espresso/latte/cappuccino): ")
    while order not in MENU.keys() and order != "report" and order != "off":
        order = input("Invalid choice, please choose one of the following - (espresso/latte/cappuccino): ")
    return order

def check_ingredients(order_ingredients):
    insufficient_resources = []
    for key, value in order_ingredients.items():
        if value > resources[key]:
            insufficient_resources.append(key)
    return insufficient_resources

def check_payment(payment, cost):
    if payment >= cost:
        return 0
    else:
        return 1

def calculate_payment(coins):
    payment = 0
    for i in range(4):
        payment += coins[i] * COINS[i]
    return payment

def take_payment():
    inserted_coins = [int(input("How many quarters?: ")), int(input("How many dimes?: ")),
                      int(input("How many nickles?: ")), int(input("How many pennies?: "))]
    return inserted_coins

def update_resources(ing):
    for key, value in ing.items():
        resources[key] -= value


while True:
    new_order = take_order()
    if new_order == "report":
        report()
        continue
    elif new_order == "off":
        break

    drink_ingredients, drink_cost = MENU[new_order].values()
    missing_ingredients = check_ingredients(drink_ingredients)
    if missing_ingredients:
        print(f"Sorry there is not enough {missing_ingredients[0]}")
        continue

    money_inserted = calculate_payment(take_payment())
    enough_payment = check_payment(money_inserted,drink_cost)
    if enough_payment == 1:
        print("Sorry that's not enough money. Money refunded.")
        continue

    update_resources(drink_ingredients)

    money += drink_cost
    if money_inserted > drink_cost:
        print(f"Here is ${money_inserted - drink_cost} in change.")

    print(f"Here is your {new_order}. Enjoy!")
