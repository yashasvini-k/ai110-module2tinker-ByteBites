import pytest
from models import Customer, MenuItem, Menu, Order

# Test 1: Order total calculates correctly
def test_calculate_total_with_multiple_items():
    burger = MenuItem("Spicy Burger", 9.99, "Food", 4.5)
    soda = MenuItem("Large Soda", 2.99, "Drinks", 4.0)
    order = Order()
    order.add_item(burger)
    order.add_item(soda)
    assert order.compute_total_cost() == 12.98

# Test 2: Empty order returns zero
def test_order_total_is_zero_when_empty():
    order = Order()
    assert order.compute_total_cost() == 0.0

# Test 3: Filter by category returns correct items
def test_filter_by_category_returns_correct_items():
    menu = Menu()
    menu.add_item(MenuItem("Large Soda", 2.99, "Drinks", 4.0))
    menu.add_item(MenuItem("Spicy Burger", 9.99, "Food", 4.5))
    drinks = menu.filter_by_category("Drinks")
    assert len(drinks) == 1
    assert drinks[0].get_name() == "Large Soda"

# Test 4: Sort by popularity returns highest rated first
def test_sort_by_popularity_returns_highest_first():
    menu = Menu()
    menu.add_item(MenuItem("Soda", 2.99, "Drinks", 3.5))
    menu.add_item(MenuItem("Burger", 9.99, "Food", 4.8))
    sorted_items = menu.sort_by_popularity()
    assert sorted_items[0].get_name() == "Burger"

# Test 5: Customer stores purchase history
def test_customer_stores_purchase_history():
    customer = Customer("Yashasvini")
    order = Order()
    customer.add_purchase(order)
    assert len(customer.get_purchase_history()) == 1