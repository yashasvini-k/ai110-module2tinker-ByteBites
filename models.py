# ByteBites Backend Models
# Four core classes:
# 1. Customer - stores name and purchase history
# 2. MenuItem - stores name, price, category, popularity rating
# 3. Menu - holds all items, can filter by category
# 4. Order - groups selected items and computes total cost


class Customer:
    def __init__(self, name):
        self.name = name
        self.purchase_history = []

    def get_name(self):
        return self.name

    def add_purchase(self, order):
        self.purchase_history.append(order)

    def get_purchase_history(self):
        return self.purchase_history


class MenuItem:
    def __init__(self, name, price, category, popularity_rating):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_category(self):
        return self.category

    def get_popularity_rating(self):
        return self.popularity_rating

    def set_popularity_rating(self, rating):
        self.popularity_rating = rating


class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_all_items(self):
        return self.items

    def filter_by_category(self, category):
        return [item for item in self.items if item.get_category() == category]


class Order:
    def __init__(self):
        self.selected_items = []
        self.total_cost = 0.0

    def add_item(self, item):
        self.selected_items.append(item)

    def remove_item(self, item):
        self.selected_items.remove(item)

    def compute_total_cost(self):
        self.total_cost = sum(item.get_price() for item in self.selected_items)
        return self.total_cost

    def get_total_cost(self):
        return self.total_cost


# --- Quick Manual Check ---
if __name__ == "__main__":
    burger = MenuItem("Spicy Burger", 9.99, "Food", 4.5)
    soda = MenuItem("Large Soda", 2.99, "Drinks", 4.0)

    menu = Menu()
    menu.add_item(burger)
    menu.add_item(soda)

    order = Order()
    order.add_item(burger)
    order.add_item(soda)
    order.compute_total_cost()

    customer = Customer("Yashasvini")
    customer.add_purchase(order)

    print("Customer:", customer.get_name())
    print("Order Total: $", order.get_total_cost())
    print("Drinks Menu:", [i.get_name() for i in menu.filter_by_category("Drinks")])