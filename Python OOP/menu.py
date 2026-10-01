class MenuItem:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price

class Menu:
    def __init__(self):
        self.items = {}

    def add_item(self, code, name, price):
        self.items[code] = MenuItem(code, name, price)

    def display(self):
        print("\n------------------ HOUSE MENU ------------------")
        print(f"{'Code':<6}{'Item Name':<30}{'Price':>10}")
        print("-" * 52)
        for item in self.items.values():
            print(f"[{item.code}]   {item.name:<29} Php {item.price:>6.2f}")
        print("-" * 52)

    def get_item(self, code):
        return self.items.get(code)