class Receipt:
    def __init__(self, cart):
        self.cart = cart

    def print_receipt(self):
        subtotal = self.cart.get_subtotal()

        print("\n" + "=" * 52)
        print("               ICHIRAKU RAMEN HOUSE                 ")
        print("                 OFFICIAL RECEIPT                   ")
        print("=" * 52)
        print(f"{'QTY':<5}{'ITEM':<27}{'PRICE':>8}{'TOTAL':>12}")
        print("-" * 52)

        for item in self.cart.items:
            print(f"{item.quantity:<5}{item.menu_item.name:<27}{item.menu_item.price:>8.2f}{item.total_item_price:>12.2f}")

        print("-" * 52)

        discount = 0.0
        if subtotal >= 800.00:
            discount = subtotal * 0.15

        grand_total = subtotal - discount

        print(f"{'SUBTOTAL:':<40} Php {subtotal:>7.2f}")
        if discount > 0:
            print(f"{'CHEF SPECIAL DISCOUNT (15%):':<40}-Php {discount:>7.2f}")
        print("=" * 52)
        print(f"{'GRAND TOTAL:':<40} Php {grand_total:>7.2f}")
        print("=" * 52)
        print("       Arigatou Gozaimasu! Please Come Again!       ")
        print("=" * 52)