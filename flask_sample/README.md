
# Flask Sample (student)

ตัวอย่างแอปเว็บด้วย Python + Flask สำหรับผู้เริ่มต้น — ใช้เพื่อเรียนรู้การสร้างเส้นทาง (routes), เทมเพลต (templates), ฟอร์ม และ API ขนาดเล็ก

## โครงสร้างโปรเจค (สั้น ๆ)

- `app.py` — ไฟล์หลักของแอปที่ประกาศ `Flask` app และกำหนด routes
- `templates/` — โฟลเดอร์สำหรับไฟล์ HTML ที่ใช้ Jinja2 templates (`layout.html`, `index.html`, `form.html`, `result.html`, `about.html`)
- `static/` — ไฟลเดอร์สำหรับไฟล์นิ่ง เช่น `css`, รูปภาพ หรือ JS (`static/css/style.css`)
- `requirements.txt` — รายการ dependencies (ที่นี่มี `Flask`)
- `.gitignore` — กำหนดไฟล์/โฟลเดอร์ที่ไม่ต้องการเก็บใน Git (`venv/` เป็นต้น)

## แนวคิดพื้นฐาน: การทำงานของ Flask แบบสั้น

- เมื่อผู้ใช้เข้า URL บนเบราว์เซอร์, Flask จะจับคู่เส้นทาง (route) กับฟังก์ชันที่เรากำหนดใน `app.py` แล้วเรียกใช้งาน
- ฟังก์ชัน route จะคืนค่า HTML (จาก `render_template`) หรือ JSON (จาก `jsonify`) หรือ redirect ตามที่ต้องการ
- เทมเพลต Jinja2 ช่วยให้เราสามารถวางตัวแปรจาก Python ลงใน HTML ได้ เช่น `{{ name }}`
- ไฟล์ใน `static/` ถูกเสิร์ฟโดยตรงที่เส้นทาง `/static/...`

## ตัวอย่างการรัน (Quick start)

```bash
cd flask_sample
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

หรือใช้ Flask CLI:

```bash
export FLASK_APP=app.py
flask run
```

เปิดเบราว์เซอร์ที่ `http://127.0.0.1:5000`

## การพัฒนา/แก้ไขเบื้องต้น

- เพิ่ม route ใหม่ใน `app.py` ด้วย decorator `@app.route('/path')`
- สร้างไฟล์ HTML ใต้ `templates/` และเรียก `render_template('file.html', var=value)`
- ใส่ CSS/JS ลงใน `static/` และอ้างถึงในเทมเพลตด้วย `/static/..`

## ถ้า `venv/` ถูกติดตามโดย Git แล้ว (เคลียร์ cache)

```bash
git rm -r --cached venv
git commit -m "Ignore venv"
```

## ไอเดียต่อยอดสำหรับผู้เรียน

- เพิ่มฟอร์มที่เก็บข้อมูลในไฟล์หรือฐานข้อมูลเล็ก ๆ (SQLite)
- สร้าง REST API เพิ่มเติม โดยคืนค่า JSON และทดลองเรียกด้วย `curl` หรือ Postman
- แยกแอปเป็นแพ็คเกจและเพิ่ม `blueprints` เพื่อจัดการหลายส่วนของแอป

มีอะไรเพิ่มเติมที่อยากให้ผมใส่ลงใน README นี้ไหม เช่น ตัวอย่างโค้ดการเชื่อม DB, Dockerfile, หรือตัวอย่าง unit test?
