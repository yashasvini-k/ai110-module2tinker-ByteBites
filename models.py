# ByteBites Backend Models
# Four core classes:
# 1. Customer - stores name and purchase history
# 2. MenuItem - stores name, price, category, popularity rating
# 3. Menu - holds all items, can filter and sort by category/rating
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

    # FILTER: returns only items matching the given category
    def filter_by_category(self, category):
        return [item for item in self.items if item.get_category() == category]

    # SORT: returns all items sorted by popularity (highest first)
    def sort_by_popularity(self):
        return sorted(self.items, key=lambda item: item.get_popularity_rating(), reverse=True)

    # SORT: returns all items sorted by price (lowest first)
    def sort_by_price(self):
        return sorted(self.items, key=lambda item: item.get_price())


class Order:
    def __init__(self):
        self.selected_items = []
        self.total_cost = 0.0

    def add_item(self, item):
        self.selected_items.append(item)

    def remove_item(self, item):
        self.selected_items.remove(item)

    def get_selected_items(self):
        return self.selected_items

    # COMPUTE: adds up the price of all selected items
    def compute_total_cost(self):
        self.total_cost = sum(item.get_price() for item in self.selected_items)
        return self.total_cost

    def get_total_cost(self):
        return self.total_cost


# --- Manual Test ---
if __name__ == "__main__":
    # Create menu items
    burger = MenuItem("Spicy Burger", 9.99, "Food", 4.5)
    soda = MenuItem("Large Soda", 2.99, "Drinks", 4.0)
    fries = MenuItem("Crispy Fries", 3.99, "Food", 4.8)
    shake = MenuItem("Chocolate Shake", 5.49, "Drinks", 3.9)

    # Build menu
    menu = Menu()
    menu.add_item(burger)
    menu.add_item(soda)
    menu.add_item(fries)
    menu.add_item(shake)

    # Test filtering
    print("=== Food Items ===")
    for item in menu.filter_by_category("Food"):
        print(" -", item.get_name())

    # Test sorting by popularity
    print("\\n=== Sorted by Popularity ===")
    for item in menu.sort_by_popularity():
        print(" -", item.get_name(), "| Rating:", item.get_popularity_rating())

    # Test sorting by price
    print("\\n=== Sorted by Price ===")
    for item in menu.sort_by_price():
        print(" -", item.get_name(), "| Price: $", item.get_price())

    # Test order total
    order = Order()
    order.add_item(burger)
    order.add_item(fries)
    order.add_item(soda)
    print("\\n=== Order Total ===")
    print("Total: $", order.compute_total_cost())

    # Test customer
    customer = Customer("Yashasvini")
    customer.add_purchase(order)
    print("\\n=== Customer ===")
    print("Name:", customer.get_name())
    print("Past Orders:", len(customer.get_purchase_history()))