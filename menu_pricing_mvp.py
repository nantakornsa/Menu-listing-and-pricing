menu_items = [
]

# =============================
# ฟังก์ชันการทำงานกับเมนู
# =============================

def show_menu(items):
    print("\n=== รายการเมนูและราคา ===")
    for item in items:
        print(f"{item['id']}. {item['name']} ({item['category']}) - {item['price']} บาท")
    print("==========================")

def search_menu(menu, keyword):
    return [m for m in menu if keyword.lower() in m["name"].lower()]

def filter_by_category(menu, category):
    return [m for m in menu if m["category"].lower() == category.lower()]

def sort_by_price(menu, desc=False):
    return sorted(menu, key=lambda x: x["price"], reverse=desc)

def load_menu_from_txt(filename="menu.txt"):
    menu = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 4:
                    id_, name, category, price = parts
                    menu.append({
                        "id": int(id_),
                        "name": name,
                        "category": category,
                        "price": int(price)
                    })
    except FileNotFoundError:
        pass  #
    return menu

def save_menu_to_txt(menu, filename="menu.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for item in menu:
            line = f"{item['id']}|{item['name']}|{item['category']}|{item['price']}\n"
            f.write(line)

def add_menu_item(menu, name, category, price):
    new_id = max([item["id"] for item in menu], default=0) + 1
    new_item = {"id": new_id, "name": name, "category": category, "price": price}
    menu.append(new_item)
    save_menu_to_txt(menu)
    print(f"✅ เพิ่มเมนู: {name} ({category}) - {price} บาท")
    return menu

def remove_menu_item(menu, item_id):
    original_len = len(menu)
    menu = [item for item in menu if item["id"] != item_id]
    if len(menu) < original_len:
        new_id = 1
        for item in menu:
            item["id"] = new_id
            new_id += 1
        save_menu_to_txt(menu)
        print(f"✅ ลบเมนู ID {item_id} เรียบร้อยแล้ว")
    else:
        print(f"❌ ไม่พบเมนูที่มี ID: {item_id}")
    return menu


# =============================
# ส่วนหลักของโปรแกรม (CLI)
# =============================

def main():
    menu = load_menu_from_txt()
    if not menu:
        menu = menu_items.copy()  # ใช้ค่าเริ่มต้นถ้าไม่มีไฟล์
        save_menu_to_txt(menu)

    while True:
        print("\n==== ระบบจัดการเมนู ====")
        print("1. แสดงเมนูทั้งหมด")
        print("2. ค้นหาเมนู")
        print("3. กรองเมนูตามหมวดหมู่")
        print("4. เรียงตามราคาน้อย -> มาก")
        print("5. เรียงตามราคามาก -> น้อย")
        print("6. เพิ่มเมนู")
        print("7. ลบเมนู")
        print("0. ออกจากโปรแกรม")

        choice = input("เลือกเมนู (0-7): ")

        if choice == "1":
            show_menu(menu)

        elif choice == "2":
            keyword = input("🔍 ป้อนคำค้นหา: ")
            results = search_menu(menu, keyword)
            if results:
                show_menu(results)
            else:
                print("❌ ไม่พบเมนูที่ค้นหา")

        elif choice == "3":
            category = input("📂 ป้อนหมวดหมู่ (เช่น Rice, Noodle, Drinks): ")
            filtered = filter_by_category(menu, category)
            if filtered:
                show_menu(filtered)
            else:
                print("❌ ไม่มีเมนูในหมวดหมู่ที่ระบุ")

        elif choice == "4":
            sorted_menu = sort_by_price(menu, desc=False)
            show_menu(sorted_menu)

        elif choice == "5":
            sorted_menu = sort_by_price(menu, desc=True)
            show_menu(sorted_menu)

        elif choice == "6":
            name = input("ชื่อเมนู: ")
            category = input("หมวดหมู่ (เช่น Rice, Drinks): ")
            try:
                price = int(input("ราคา (บาท): "))
                menu = add_menu_item(menu, name, category, price)
            except ValueError:
                print("❌ ราคาต้องเป็นตัวเลข")

        elif choice == "7":
            try:
                item_id = int(input("ใส่ ID เมนูที่ต้องการลบ: "))
                menu = remove_menu_item(menu, item_id)
            except ValueError:
                print("❌ ID ต้องเป็นตัวเลข")

        elif choice == "0":
            print("👋 ออกจากโปรแกรมแล้ว")
            break

        else:
            print("⚠️ กรุณาเลือกเมนูให้ถูกต้อง")


if __name__ == "__main__":
    main()
