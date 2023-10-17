from menu import MENU

#function to request the user to insert money, it then calculates it and returns the total
def request_payment():
    print("Please insert coins")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))
    total = (quarters *0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    return total

#Function to check if the payment is enough for the choice selected
def check_payment(coffee, payment):
    cost = MENU[coffee]['cost']
    if payment >= cost:
        return True
    else:
        return False

#Calculates the change due to buyer
def change(payment, cost):
    return payment - cost

#Function to check how much resources are left in the machine
def get_resources():
    print(f"Water: {resources_available['Water']}ml")
    print(f"Milk: {resources_available['Milk']}ml")
    print(f"Coffee: {resources_available['Coffee']}g")
    print(f"Money: ${resources_available['Money']}")

#Function that calculates how much resources ar eleft after a purchase
def use_resources(coffee):
    resources_available['Water'] -= MENU[choice]["ingredients"]["water"]
    resources_available['Coffee'] -= MENU[choice]["ingredients"]["coffee"]
    resources_available['Money'] += MENU[choice]["cost"]
    if coffee != "espresso":
        resources_available['Milk'] -= MENU[choice]["ingredients"]["milk"]

#Function to check if there is enough resources to service the buyer with the required coffee
def check_enough_resources(coffee):
    resource_status = True
    if resources_available['Water'] < MENU[choice]["ingredients"]["water"]:
        print("Sorry there is not enough water")
        resource_status = False
    elif resources_available['Coffee'] < MENU[choice]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee")
        resource_status = False
    elif resources_available['Coffee'] < MENU[choice]["ingredients"]["coffee"] and coffee != "espresso":
        print("Sorry there is not enough milk")
        resource_status = False
    return resource_status

#Dictionary of the resources
resources_available = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money": 0
}

#Variables for the coins
quaters = 0
dimes = 0
nickles = 0
pennies = 0

#variable for the change due to buyer
give_back = 0

#Variables for the loop
keep_ordering = True

#variable to check if we have enough resources to honour the purchase
check_resources = True

while keep_ordering:
    choice = input("What would you like? (espresso/latte/cappuccino: ").lower()

    if choice == "report":
        get_resources()
    elif choice == "latte":
        check_resources = check_enough_resources(choice)
        if check_resources == True:
            payment = request_payment()
            if check_payment(choice, payment):
                use_resources(choice)
                give_back = round(change(payment,MENU[choice]["cost"]), 2)
                if give_back > 0:
                    print(f"Here is ${give_back} in change.")
                print(f"Here is your {choice} Enjoy!")
            else:
                print("Sorry, that's not enough money. Money refunded.")
    elif choice == "cappuccino":
        check_resources = check_enough_resources(choice)
        if check_resources == True:
            payment = request_payment()
            if check_payment(choice, payment):
                use_resources(choice)
                give_back = round(change(payment,MENU[choice]["cost"]), 2)
                if give_back > 0:
                    print(f"Here is ${give_back} in change")
                print(f"Here is your {choice} Enjoy!")
            else:
                print("Sorry, that's not enough money. Money refunded.")
                give_back = 0
    elif choice == "espresso":
        check_resources = check_enough_resources(choice)
        if check_resources == True:
            payment = request_payment()
            if check_payment(choice, payment):
                use_resources(choice)
                give_back = round(change(payment,MENU[choice]["cost"]), 2)
                if give_back > 0:
                    print(f"Here is ${give_back} in change.")
                print(f"Here is your {choice} Enjoy!")
            else:
                print("Sorry, that's not enough money. Money refunded.")
                give_back = 0
    else:
        print("Coffee Machine Shutting down...")
        break




