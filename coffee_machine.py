# Initial resources and money
resources = {
    "water": 2000,    
    "milk": 1000,     
    "coffee": 500,    
    "money": 0        
}

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "cost": 2.50
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150
        },
        "cost": 3.50
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100
        },
        "cost": 3.00
    }
}

def print_report():
    """Print current resource levels"""
    print("\n-------- RESOURCE REPORT --------")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}")
    print("--------------------------------")

def check_resources(drink_choice):
    """Check if there are enough resources to make the drink"""
    for item, amount in MENU[drink_choice]["ingredients"].items():
        if resources[item] < amount:
            print(f"\nSorry, not enough {item}!")
            return False
    return True

def process_coins():
    """Process inserted coins and return total"""
    print("\nPlease insert coins:")
    try:
        quarters = int(input("Quarters (0.25): ")) * 0.25
        dimes = int(input("Dimes (0.10): ")) * 0.10
        nickels = int(input("Nickels (0.05): ")) * 0.05
        pennies = int(input("Pennies (0.01): ")) * 0.01
        return quarters + dimes + nickels + pennies
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        return 0

def make_coffee(drink_choice, payment):
    """Make coffee if payment is sufficient and update resources"""
    drink_cost = MENU[drink_choice]["cost"]
    
    if payment < drink_cost:
        print(f"\nSorry, that's not enough money. You need ${drink_cost:.2f}")
        print(f"Money refunded: ${payment:.2f}")
        return False
    
    change = payment - drink_cost
    if change > 0:
        print(f"\nHere's your change: ${change:.2f}")
    
    for item, amount in MENU[drink_choice]["ingredients"].items():
        resources[item] -= amount
    
    resources["money"] += drink_cost
    print(f"\nHere's your {drink_choice}! ☕️ Enjoy!")
    return True

def print_menu():
    """Print the menu with prices"""
    print("\n======= COFFEE MENU =======")
    for drink, info in MENU.items():
        print(f"{drink.title()}: ${info['cost']:.2f}")
    print("=========================")

def main():
    while True:
        print_menu()
        choice = input("\nWhat would you like? (espresso/latte/cappuccino)\n"
                      "Enter 'report' to check resources or 'off' to exit: ").lower()
        
        if choice == "off":
            print("\nShutting down. Goodbye!")
            break
            
        elif choice == "report":
            print_report()
            
        elif choice in MENU:
            if check_resources(choice):
                payment = process_coins()
                make_coffee(choice, payment)
                
        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    main()