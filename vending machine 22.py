class VendingMachine:
    def __init__(self):
        # Initialize product catalog with codes, prices, categories, and number in stock
        self.products = {
            "A1": {"name": "Soda", "price": 1.50, "quantity": 10, "category": "Drinks"},
            "A2": {"name": "Chips", "price": 1.00, "quantity": 10, "category": "Snacks"},
            "A3": {"name": "Candy", "price": 0.75, "quantity": 10, "category": "Snacks"},
            "B1": {"name": "Water", "price": 1.00, "quantity": 10, "category": "Drinks"},
            "B2": {"name": "Juice", "price": 1.75, "quantity": 10, "category": "Drinks"},
            "C1": {"name": "Coffee", "price": 2.00, "quantity": 5, "category": "Hot Drinks"},
            "C2": {"name": "Biscuits", "price": 1.20, "quantity": 10, "category": "Snacks"}
        }
        self.balance = 0.0
        self.previous_purchase = None

    def show_menu(self):
        # Displays the menu of available drinks and snacks along with codes, prices, categories, and quantities
        print("\nWelcome to the Vending Machine!")
        categories = set(product["category"] for product in self.products.values())  # Get unique categories
        for category in categories:
            print(f"\n{category}:")
            for code, product in self.products.items():
                if product["category"] == category:
                    print(f"{code}. {product['name']} - £{product['price']} (Stock: {product['quantity']})")
        print("")

    def select_product(self):
        # Allow the user to choose a product by code
        code = input("Please enter the code for the product you want to buy: ").upper()
        if code not in self.products:
            print("Invalid code. Please try again.")
            return None
        elif self.products[code]["quantity"] == 0:
            print(f"Sorry, {self.products[code]['name']} is out of stock.")
            return None
        return code

    def process_payment(self, product_code):
        # Process the payment for the selected product
        price = self.products[product_code]["price"]
        while True:
            try:
                print(f"The price of {self.products[product_code]['name']} is £{price}. Please insert money.")
                money_inserted = float(input("Enter the amount of money: £"))
                if money_inserted < price:
                    print(f"Insufficient amount. Please insert at least £{price}.")
                elif money_inserted == price:
                    self.balance += price
                    self.products[product_code]["quantity"] -= 1
                    print(f"Exact amount received. Enjoy your {self.products[product_code]['name']}!")
                    break
                else:
                    change = money_inserted - price
                    self.balance += price
                    self.products[product_code]["quantity"] -= 1
                    print(f"Transaction successful. Your change is £{change:.2f}. Enjoy your {self.products[product_code]['name']}!")
                    break
            except ValueError:
                print("Invalid input. Please enter a valid amount.")

    def suggest_purchase(self):
        # Suggest a product based on the previous purchase (if applicable)
        if self.previous_purchase:
            if self.previous_purchase["category"] == "Hot Drinks":
                print("Since you bought a Hot Drink, you might also like to buy some Biscuits!")
            elif self.previous_purchase["category"] == "Drinks":
                print("Would you like to buy some Chips or Candy to go with your drink?")
            elif self.previous_purchase["category"] == "Snacks":
                print("How about grabbing a refreshing drink to go with your snack?")
        else:
            print("Would you like to buy something else?")

    def run_machine(self):
        # Run the Vending Machine program
        while True:
            self.show_menu()
            product_code = self.select_product()
            if product_code:
                self.process_payment(product_code)
                self.previous_purchase = self.products[product_code]  # Store the last purchased item
                self.suggest_purchase()  # Suggest items based on the last purchase
            continue_choice = input("Would you like to buy another product? (y/n): ").lower()
            if continue_choice != 'y':
                print(f"Thank you for using the vending machine! Total balance: £{self.balance:.2f}")
                break


# Main Program
if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.run_machine()
