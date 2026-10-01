import sys
from menu import Menu
from cart import Cart
from receipt import Receipt

class OrderApp:
    def __init__(self):
        self.menu = Menu()
        self.cart = Cart()
        self._load_menu()

    def _load_menu(self):
        menu_data = {
            1: {"name": "Shoyu Ramen", "price": 320.00},
            2: {"name": "Tonkotsu Ramen", "price": 350.00},
            3: {"name": "Chicken Teriyaki", "price": 250.00},
            4: {"name": "Pork Gyoza (6 pcs)", "price": 180.00},
            5: {"name": "Takoyaki (6 pcs)", "price": 150.00},
            6: {"name": "Japanese Iced Tea", "price": 80.00}
        }
        for code, item in menu_data.items():
            self.menu.add_item(code, item["name"], item["price"])

    def display_header(self):
        print("=" * 52)
        print("         ICHIRAKU RAMEN HOUSE (一楽ラーメン)         ".center(52))
        print("=" * 52)

    def get_valid_integer(self, prompt):
        while True:
            try:
                value = int(input(prompt))
                if value > 0:
                    return value
                else:
                    print("[!] Error: Value must be a positive integer.")
            except ValueError:
                print("[!] Error: Invalid entry! Please enter numbers only.")

    def run(self):
        self.display_header()
        self.menu.display()

        while True:
            start_order = input("\nWould you like to place an order? (yes/no): ").strip().lower()
            if start_order in ['yes', 'y', 'no', 'n']:
                break
            print("[!] Error: Please enter 'yes' or 'no'.")

        if start_order in ['no', 'n']:
            print("\nThank you for visiting Ichiraku Ramen House!")
            sys.exit()

        while True:
            item_code = self.get_valid_integer("\nEnter Item Code to order: ")
            menu_item = self.menu.get_item(item_code)

            if not menu_item:
                print("[!] Error: Item code not found in menu. Try again.")
                continue

            quantity = self.get_valid_integer(f"Enter quantity for {menu_item.name}: ")
            self.cart.add_item(menu_item, quantity)

            print(f"[✓] Added {quantity} x {menu_item.name} to your cart.")

            while True:
                more = input("\nWould you like to order another item? (yes/no): ").strip().lower()
                if more in ['yes', 'y', 'no', 'n']:
                    break
                print("[!] Error: Please respond with 'yes' or 'no'.")

            if more in ['no', 'n']:
                break

        receipt = Receipt(self.cart)
        receipt.print_receipt()

if __name__ == "__main__":
    app = OrderApp()
    app.run()