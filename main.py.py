import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Import resources and recipes from data.py
resources = data.resources
recipes = data.recipes

# Instantiate the objects
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    is_on = True

    while is_on:
        choice = input("What size sandwich would you like? (small/ medium/ large/ off/ report): ").lower()

        if choice == "off":
            is_on = False
        elif choice == "report":
            print(f"Bread: {sandwich_maker_instance.machine_resources['bread']} slice(s)")
            print(f"Ham: {sandwich_maker_instance.machine_resources['ham']} slice(s)")
            print(f"Cheese: {sandwich_maker_instance.machine_resources['cheese']} oz")
        elif choice in recipes:
            sandwich = recipes[choice]
            ingredients = sandwich["ingredients"]
            cost = sandwich["cost"]

            # Step 1: Check if resources are sufficient
            if sandwich_maker_instance.check_resources(ingredients):
                # Step 2: Process coin input
                payment = cashier_instance.process_coins()

                # Step 3: Check transaction success and serve sandwich
                if cashier_instance.transaction_result(payment, cost):
                    sandwich_maker_instance.make_sandwich(choice, ingredients)
        else:
            print("Invalid selection. Please choose small, medium, large, report, or off.")


if __name__ == "__main__":
    main()
