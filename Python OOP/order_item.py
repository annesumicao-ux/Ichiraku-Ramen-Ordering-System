class OrderItem:
    def __init__(self, menu_item, quantity):
        self.menu_item = menu_item
        self.quantity = quantity
        self.total_item_price = menu_item.price * quantity