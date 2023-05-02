import items

money = 0

def resources():
    water, milk, coffee = items.resources.values()
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money:.2f}")

def check_ingredients(choice):
    ingredients = items.MENU[choice]['ingredients']
    for ingredient, amount in ingredients.items():
        if items.resources[ingredient] < amount:
            print(f"You don't have enough {ingredient}")
            return False
    return True

def process_payment(cost):
    global money
    if money < cost:
        print("Please insert coins.")
        money += (int(input("How many quarters?: ")) / 4)
        money += (int(input("How many dimes?: ")) / 10)
        money += (int(input("How many nickles?: ")) / 20)
        money += (int(input("How many pennies?: ")) / 100) 
        if money < cost:
            print("Sorry that's not enough money. Money refunded")
            money = 0
            return False
    money -= cost
    return True

def make_drink(choice):
    ingredients = items.MENU[choice]['ingredients']
    for ingredient, amount in ingredients.items():
        items.resources[ingredient] -= amount
    print(f"Here is your {choice}. Enjoy!")

while True:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == 'report':
        resources()
    elif choice in ('espresso', 'latte', 'cappuccino'):
        if check_ingredients(choice) and process_payment(items.MENU[choice]['cost']):
            make_drink(choice)
    else:
        print("Sorry, that's not a valid choice. Please try again")
