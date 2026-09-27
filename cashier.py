class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        dollars = float(input("how many dollars?: ") or 0)
        half_dollars = float(input("how many half dollars?: ") or 0) * 0.5
        quarters = float(input("how many quarters?: ") or 0) * 0.25
        nickels = float(input("how many nickels?: ") or 0) * 0.05
        
        total = dollars + half_dollars + quarters + nickels
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient."""
        if coins >= cost:
            change = round(coins - cost, 2)
            if change > 0:
                print(f"Here is ${change:.2f} in change.")
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False
