from helpers import get_valid_integer

def display_header():
    print("=" * 52)
    print("         ICHIRAKU RAMEN HOUSE (一楽ラーメン)         ".center(52))
    print("=" * 52)

def display_menu(menu_dict):
    print("\n------------------ HOUSE MENU ------------------")
    print(f"{'Code':<6}{'Item Name':<30}{'Price':>10}")
    print("-" * 52)
    for item_code, item_info in menu_dict.items():
        print(f"[{item_code}]   {item_info['name']:<29} Php {item_info['price']:>6.2f}")
    print("-" * 52)

def take_orders(menu_dict):
    cart = []

    while True:
        item_code = get_valid_integer("\nEnter Item Code to order: ")

        if item_code not in menu_dict:
            print("[!] Error: Item code not found in menu. Try again.")
            continue

        quantity = get_valid_integer(f"Enter quantity for {menu_dict[item_code]['name']}: ")

        cart.append({
            "name": menu_dict[item_code]["name"],
            "price": menu_dict[item_code]["price"],
            "quantity": quantity,
            "total_item_price": menu_dict[item_code]["price"] * quantity
        })

        print(f"[✓] Added {quantity} x {menu_dict[item_code]['name']} to your cart.")

        while True:
            more = input("\nWould you like to order another item? (yes/no): ").strip().lower()
            if more in ['yes', 'y', 'no', 'n']:
                break
            print("[!] Error: Please respond with 'yes' or 'no'.")

        if more in ['no', 'n']:
            break

    return cart

def print_receipt(cart):
    subtotal = 0.0

    print("\n" + "=" * 52)
    print("               ICHIRAKU RAMEN HOUSE                 ")
    print("                 OFFICIAL RECEIPT                   ")
    print("=" * 52)
    print(f"{'QTY':<5}{'ITEM':<27}{'PRICE':>8}{'TOTAL':>12}")
    print("-" * 52)

    for item in cart:
        subtotal += item["total_item_price"]
        print(f"{item['quantity']:<5}{item['name']:<27}{item['price']:>8.2f}{item['total_item_price']:>12.2f}")

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