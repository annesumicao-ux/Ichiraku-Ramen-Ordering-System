from order_item import OrderItem

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, menu_item, quantity):
        order_item = OrderItem(menu_item, quantity)
        self.items.append(order_item)

    def get_subtotal(self):
        return sum(item.total_item_price for item in self.items)