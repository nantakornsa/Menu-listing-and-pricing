import json

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


def load_menu_from_json(filename="menu.json"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_menu_to_json(menu, filename="menu.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(menu, f, ensure_ascii=False, indent=4)


def add_menu_item(menu, name, category, price):
    new_id = max([item["id"] for item in menu], default=0) + 1
    new_item = {"id": new_id, "name": name, "category": category, "price": price}
    menu.append(new_item)
    save_menu_to_json(menu)
    print(f"✅ เพิ่มเมนู: {name} ({category}) - {price} บาท")
    return menu


def remove_menu_item(menu, item_id):
    original_len = len(menu)
    menu = [item for item in menu if item["id"] != item_id]
    if len(menu) < original_len:
        # รีเซต ID ใหม่ให้เรียงลำดับ
        new_id = 1
        for item in menu:
            item["id"] = new_id
            new_id += 1

        save_menu_to_json(menu)
        print(f"✅ ลบเมนู ID {item_id} เรียบร้อยแล้ว")
    else:
        print(f"❌ ไม่พบเมนูที่มี ID: {item_id}")
    return menu

def load_menu_from_json(filename="menu.json"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # ถ้าไฟล์ยังไม่มี -> สร้างไฟล์ใหม่เป็น list ว่าง
        save_menu_to_json([])
        return []




# =============================
# ส่วนหลักของโปรแกรม (CLI)
# =============================

def main():
    menu = load_menu_from_json()
    admin_password = "1234"

    while True:  # loop สำหรับเลือก Role
        print("\n==========================")
        print("Admin or customer?")
        print("Press A if you are Admin")
        print("Press B if you are Customer")
        print("Press Q to Quit")
        print("==========================")

        Role_selection = input("Please select your role: ").lower()
        if Role_selection == "q":
            print("👋 ออกจากโปรแกรมแล้ว")
            break

        if Role_selection not in ["a", "b"]:
            print("❌ You can only choose a or b")
            continue

        # ==== Admin ====
        if Role_selection == "a":
            password = input("🔑 กรุณากรอกรหัสผ่านเจ้าของร้าน: ")
            if password != admin_password:
                print("❌ รหัสผ่านไม่ถูกต้อง! กลับไปหน้าเลือก role")
                continue

            # loop ของเมนู Admin
            while True:
                print("\n==== ระบบจัดการเมนู (Admin) ====")
                print("1. แสดงเมนูทั้งหมด")
                print("2. ค้นหาเมนู")
                print("3. กรองเมนูตามหมวดหมู่")
                print("4. เรียงตามราคาน้อย -> มาก")
                print("5. เรียงตามราคามาก -> น้อย")
                print("6. เพิ่มเมนู")
                print("7. ลบเมนู")
                print("8. กลับไปเลือก Role")
                print("0. ออกจากโปรแกรม")

                choice = input("เลือกเมนู (0-8): ")

                if choice == "1":
                    show_menu(menu)
                elif choice == "2":
                    keyword = input("🔍 ป้อนคำค้นหา: ")
                    results = search_menu(menu, keyword)
                    show_menu(results) if results else print("❌ ไม่พบเมนูที่ค้นหา")
                elif choice == "3":
                    category = input("📂 ป้อนหมวดหมู่: ")
                    filtered = filter_by_category(menu, category)
                    show_menu(filtered) if filtered else print("❌ ไม่มีเมนูในหมวดหมู่ที่ระบุ")
                elif choice == "4":
                    show_menu(sort_by_price(menu))
                elif choice == "5":
                    show_menu(sort_by_price(menu, desc=True))
                elif choice == "6":
                    name = input("ชื่อเมนู: ")
                    category = input("หมวดหมู่: ")
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
                elif choice == "8":
                    print("↩️ กลับไปเลือก Role ใหม่")
                    break   # ออกจาก loop ของ Admin → กลับไปเลือก Role
                elif choice == "0":
                    print("👋 ออกจากโปรแกรมแล้ว")
                    return
                else:
                    print("⚠️ กรุณาเลือกเมนูให้ถูกต้อง")

        # ==== Customer ====
        elif Role_selection == "b":
            while True:
                print("\n==== เมนูสำหรับลูกค้า ====")
                print("1. แสดงเมนูทั้งหมด")
                print("2. ค้นหาเมนู")
                print("3. กรองเมนูตามหมวดหมู่")
                print("4. เรียงตามราคาน้อย -> มาก")
                print("5. เรียงตามราคามาก -> น้อย")
                print("6. กลับไปเลือก Role")
                print("0. ออกจากโปรแกรม")

                choice = input("เลือกเมนู (0-6): ")

                if choice == "1":
                    show_menu(menu)
                elif choice == "2":
                    keyword = input("🔍 ป้อนคำค้นหา: ")
                    results = search_menu(menu, keyword)
                    show_menu(results) if results else print("❌ ไม่พบเมนูที่ค้นหา")
                elif choice == "3":
                    category = input("📂 ป้อนหมวดหมู่: ")
                    filtered = filter_by_category(menu, category)
                    show_menu(filtered) if filtered else print("❌ ไม่มีเมนูในหมวดหมู่ที่ระบุ")
                elif choice == "4":
                    show_menu(sort_by_price(menu))
                elif choice == "5":
                    show_menu(sort_by_price(menu, desc=True))
                elif choice == "6":
                    print("↩️ กลับไปเลือก Role ใหม่")
                    break   # ออกจาก loop ของ Customer → กลับไปเลือก Role
                elif choice == "0":
                    print("👋 ออกจากโปรแกรมแล้ว")
                    return
                else:
                    print("⚠️ กรุณาเลือกเมนูให้ถูกต้อง")



if __name__ == "__main__":
    main()
