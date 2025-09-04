# Menu Listing & Pricing — Sprint 1 (Week 1)

MVP: แสดงรายการเมนูและราคาได้จริง (อ่านจาก data ภายในโปรเจกต์), มีการจัดรูปแบบราคา, ค้นหา, กรองหมวดหมู่, จัดเรียง, และจัดการกรณี "ไม่มีรายการ"

## Sprint Goal
- ลูกค้าเห็นเมนูและราคา (read-only)
- มีการกรอง/ค้นหา/เรียงขั้นพื้นฐาน
- มี test cases แบบ manual สำหรับ Debugger

## Roles
- **ออโต้ (Planner)**: สร้าง Issues/Project Board, แตกงานเป็น Task, นิยาม DoD (Definition of Done)
- **ทีน (Coder)**: พัฒนา `src/app.js`, `src/data.js`, สร้าง UI ใน `index.html` + `styles.css`
- **ลูกหมู (Debugger)**: ทดสอบตาม `tests` ใน README ด้านล่าง, เปิดบั๊กเป็น Issues พร้อม Steps

## Run
เปิด `index.html` ตรง ๆ ได้เลย (ไม่ต้องติดตั้งอะไร)

> ถ้าจะใช้ Live Server ใน VS Code: คลิกขวา `index.html` → **Open with Live Server**

## Project Board (แนะนำตั้งใน GitHub Projects)
**Columns:** Backlog → In Progress → In Review/Testing → Done

## Issues (ตัวอย่าง)
1. Setup repo & scaffolding
2. Render menu list from `data.js`
3. Implement price formatter (THB/locale-aware)
4. Add category filter + search
5. Add sort (Name/Price)
6. Empty/invalid data states
7. Accessibility pass (tab order, ARIA)
8. Manual test cases execution
9. Bugfix from testing feedback

## Definition of Done (Sprint 1)
- แสดงเมนูได้ครบ/ถูกต้อง (เฉพาะที่ available)
- ค้นหา/กรอง/เรียง ทำงานได้พร้อมกัน
- กรณีเมนูว่าง แสดงข้อความเตือนผู้ใช้
- โค้ดผ่าน review (PR) + ไม่มี error ใน Console

## Manual Test Cases (ย่อ)
1. **Load Success**: เปิดหน้าแล้วเห็นเมนู ≥ 1 รายการ
2. **Search**: พิมพ์ "rice" แล้วผลลัพธ์เหลือเฉพาะรายการที่ชื่อ/หมวด/คำอธิบายมีคำนี้
3. **Filter Category**: เลือก "Drinks" แล้วเหลือเฉพาะหมวดนั้น
4. **Sort**: เปลี่ยน Sort เป็น Price (Low→High) แล้วเรียงถูก
5. **Unavailable**: รายการที่ `available=false` ไม่ปรากฏ
6. **Empty State**: เคลียร์ search ให้ไม่ตรงกับอะไร → เห็นข้อความ "ไม่พบเมนู"
7. **Invalid Price**: (มีใน data ทดสอบ) ต้องไม่ทำให้หน้าเออเรอร์ และแสดง "N/A"

## Conventions
- Branch: `feature/<short-desc>` / `fix/<short-desc>`
- Commits (ตัวอย่าง): `feat: add category filter`, `fix: handle invalid price`
- PR: ใช้เทมเพลต `.github/PULL_REQUEST_TEMPLATE.md`

## License
MIT
