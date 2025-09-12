menu_items = [
    {"id": 1, "name": "ข้าวกะเพราไก่ไข่ดาว", "category": "Rice", "price": 55},
    {"id": 2, "name": "ข้าวผัดหมู", "category": "Rice", "price": 50},
    {"id": 3, "name": "ผัดไทยกุ้งสด", "category": "Noodle", "price": 75},
    {"id": 4, "name": "ชาไทย", "category": "Drinks", "price": 25},
    {"id": 5, "name": "น้ำเปล่า", "category": "Drinks", "price": 10},
]

def show_menu(items):
    print("\n=== รายการเมนูและราคา ===")
    for item in items:
        print(f"{item['id']}. {item['name']} ({item['category']}) - {item['price']} บาท")
    print("==========================")

def search_menu(keyword):
    return [m for m in menu_items if keyword.lower() in m["name"].lower()]

def filter_by_category(category):
    return [m for m in menu_items if m["category"].lower() == category.lower()]

def sort_by_price(desc=False):
    return sorted(menu_items, key=lambda x: x["price"], reverse=desc)

def main():
    while True:
        print("\n==== ระบบจัดการเมนู ====")
        print("1. แสดงเมนูทั้งหมด")
        print("2. ค้นหาเมนู")
        print("3. กรองเมนูตามหมวดหมู่")
        print("4. แสดงเมนูเรียงเมนูตามราคา (น้อย -> มาก)")
        print("5. แสดงเมนูเรียงเมนูตามราคา (มาก -> น้อย)")
        print("0. ออกจากโปรแกรม")

        choice = input("เลือกเมนู (0-5): ")

        if choice == "1":
            show_menu(menu_items)
        elif choice == "2":
            keyword = input("🔍 ป้อนคำค้นหา: ")
            results = search_menu(keyword)
            show_menu(results) if results else print("❌ ไม่พบเมนูที่ค้นหา")
        elif choice == "3":
            category = input("📂 ป้อนหมวดหมู่ (เช่น Rice, Noodle, Drinks): ")
            filtered = filter_by_category(category)
            show_menu(filtered) if filtered else print("❌ ไม่มีเมนูในหมวดหมู่ที่ระบุ")
        elif choice == "4":
            show_menu(sort_by_price(desc=False))
        elif choice == "5":
            show_menu(sort_by_price(desc=True))
        elif choice == "0":
            print("👋 ออกจากโปรแกรมแล้ว")
            break
        else:
            print("⚠️ กรุณาเลือกเมนูให้ถูกต้อง")

if __name__ == "__main__":
    main()
