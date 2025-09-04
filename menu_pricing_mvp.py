import json

# Load menu data
with open("data/sample_menu.json", "r", encoding="utf-8") as f:
    menu = json.load(f)

# --- Functions ---
def show_menu():
    print("\n--- All Menu ---")
    for item in menu:
        print(f"[{item['category']}] {item['name']} - {item['price']} THB")

def search_menu(keyword: str):
    print(f"\n--- Search: '{keyword}' ---")
    results = [item for item in menu if keyword.lower() in item['name'].lower()]
    if results:
        for item in results:
            print(f"[{item['category']}] {item['name']} - {item['price']} THB")
    else:
        print("No menu found.")

def filter_by_category(category: str):
    print(f"\n--- Filter: {category} ---")
    results = [item for item in menu if item['category'].lower() == category.lower()]
    if results:
        for item in results:
            print(f"[{item['category']}] {item['name']} - {item['price']} THB")
    else:
        print("No menu in this category.")

def sort_by_price(desc=False):
    order = "DESC" if desc else "ASC"
    print(f"\n--- Sorted by price {order} ---")
    sorted_menu = sorted(menu, key=lambda x: x['price'], reverse=desc)
    for item in sorted_menu:
        print(f"[{item['category']}] {item['name']} - {item['price']} THB")

# --- Demo run ---
if __name__ == "__main__":
    show_menu()
    search_menu("Tea")
    filter_by_category("Drink")
    sort_by_price()
    sort_by_price(desc=True)
