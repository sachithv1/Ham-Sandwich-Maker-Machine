### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,   ## slice
            "ham": 4,     ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,   ## slice
            "ham": 6,     ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,   ## slice
            "ham": 8,     ## slice
            "cheese": 12, ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,   ## slice
    "ham": 18,     ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item, amount in ingredients.items():
            if self.machine_resources.get(item, 0) < amount:
                print(f"Sorry, there is not enough {item}.")
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")
        try:
            dollars = int(input("how many dollars?: ") or 0)
            half_dollars = int(input("how many half dollars?: ") or 0)
            quarters = int(input("how many quarters?: ") or 0)
            nickels = int(input("how many nickels?: ") or 0)
        except ValueError:
            print("Invalid input for coins. Treating non-digit entry as 0.")
            dollars, half_dollars, quarters, nickels = 0, 0, 0, 0

        total = (dollars * 1.0) + (half_dollars * 0.5) + (quarters * 0.25) + (nickels * 0.05)
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            change = round(coins - cost, 2)
            if change > 0:
                print(f"Here is ${change:.2f} in change.")
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for item, amount in order_ingredients.items():
            self.machine_resources[item] -= amount
        print(f"{sandwich_size.capitalize()} sandwich is ready. Bon appetit!")


### Make an instance of SandwichMachine class and write the rest of the codes ###

def main():
    machine = SandwichMachine(resources)
    is_on = True

    while is_on:
        choice = input("What would you like? (small/medium/large/report/off): ").strip().lower()

        if choice == "off":
            is_on = False
            print("Turning off the machine. Goodbye!")

        elif choice == "report":
            print(f"Bread: {machine.machine_resources['bread']} slice(s)")
            print(f"Ham: {machine.machine_resources['ham']} slice(s)")
            print(f"Cheese: {machine.machine_resources['cheese']} oz")

        elif choice in recipes:
            sandwich = recipes[choice]
            ingredients = sandwich["ingredients"]
            cost = sandwich["cost"]

            # 1. Check if resources are sufficient
            if machine.check_resources(ingredients):
                # 2. Process coins inserted by user
                inserted_coins = machine.process_coins()
                # 3. Verify transaction and make sandwich if successful
                if machine.transaction_result(inserted_coins, cost):
                    machine.make_sandwich(choice, ingredients)

        else:
            print("Invalid option. Please choose small, medium, large, report, or off.")

if __name__ == "__main__":
    main()