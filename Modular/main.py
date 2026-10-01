import sys
from config import MENU
from order_system import display_header, display_menu, take_orders, print_receipt

def main():
    display_header()
    display_menu(MENU)

    while True:
        start_order = input("\nWould you like to place an order? (yes/no): ").strip().lower()
        if start_order in ['yes', 'y', 'no', 'n']:
            break
        print("[!] Error: Please enter 'yes' or 'no'.")

    if start_order in ['no', 'n']:
        print("\nThank you for visiting Ichiraku Ramen House!")
        sys.exit()

    order_cart = take_orders(MENU)
    print_receipt(order_cart)

if __name__ == "__main__":
    main()