
# Flask Sample (student)

ตัวอย่างแอปเว็บด้วย Python + Flask สำหรับผู้เริ่มต้น — ใช้เพื่อเรียนรู้การสร้างเส้นทาง (routes), เทมเพลต (templates), ฟอร์ม และ API ขนาดเล็ก

## โครงสร้างโปรเจค (พื้นฐานที่ใช้งานได้จริง)

- `app.py` — ไฟล์หลักของแอปที่ประกาศ `Flask` app และกำหนด routes
- `templates/` — โฟลเดอร์สำหรับไฟล์ HTML ที่ใช้ Jinja2 templates (`layout.html`, `index.html`, `form.html`, `result.html`, `about.html`)
- `static/` — ไฟลเดอร์สำหรับไฟล์นิ่ง เช่น `css`, รูปภาพ หรือ JS (`static/css/style.css`)
- `requirements.txt` — รายการ dependencies (ที่นี่มี `Flask`)
- `.gitignore` — กำหนดไฟล์/โฟลเดอร์ที่ไม่ต้องการเก็บใน Git (`venv/` เป็นต้น)

## แนวคิดพื้นฐาน: การทำงานของ Flask 

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


## คำอธิบายโค้ด (ตาม `app.py`) — รายข้อ

1. ความหมายของ `app = Flask(__name__)`

	- บรรทัดนี้สร้างอินสแตนซ์ของคลาส `Flask` และเก็บไว้ในตัวแปร `app` ซึ่งเราใช้เป็นตัวแทนแอปพลิเคชันทั้งหมด
	- พารามิเตอร์ `__name__` บอกชื่อโมดูลปัจจุบันให้ Flask ใช้ในการค้นหาไฟล์เทมเพลต (`templates/`) และไฟล์ static (`static/`) และใช้ในการตั้งค่าการโหลดไฟล์เมื่อรันเป็นโมดูลหรือสคริปต์

2. `@app.route('/')`, `@app.route('/about')` และ `@app.route('/greet', methods=['GET', 'POST'])`

	- `@app.route(...)` เป็น decorator ที่ใช้ลงทะเบียน URL endpoint กับฟังก์ชันใน `app.py` เช่น `index()`, `about()` และ `greet()`
	- เมื่อมีคำขอ HTTP มาที่ URL ที่ตรงกับ route นั้น Flask จะเรียกใช้งานฟังก์ชันที่ถูกตกแต่งและนำค่าที่คืนกลับไปเป็นคำตอบ (response)
	- การระบุ `methods=['GET', 'POST']` จะอนุญาตให้รับคำขอทั้งแบบ GET และ POST สำหรับเส้นทางนั้น (ถ้าไม่ระบุ จะเป็น GET เท่านั้น)

3. การทำงาน GET / POST, `request.method`, `request.form.get`

	- GET: มักใช้เพื่อดึงข้อมูลหรือแสดงฟอร์ม เช่น เมื่อเข้า `/greet` ด้วย GET จะส่งกลับหน้า `form.html` เพื่อให้ผู้ใช้กรอกชื่อ
	- POST: มักใช้เมื่อส่งข้อมูลจากฟอร์มหรือเมื่ออยากเปลี่ยนสถานะที่ฝั่งเซิร์ฟเวอร์ เช่น เมื่อฟอร์มส่งแบบ POST จะมีการประมวลผลข้อมูลและคืนหน้า `result.html`
	- `request.method` เป็นวิธีตรวจสอบว่า HTTP request ปัจจุบันเป็น GET หรือ POST (หรืออื่น ๆ)
	- `request.form.get('name', 'Student')` อ่านค่าจากข้อมูลฟอร์มที่ถูกส่งมาทาง POST (หรือจาก body ของคำขอแบบ form-encoded) โดย `.get()` มีอาร์กิวเมนต์ตัวที่สองเป็นค่าเริ่มต้นถ้าไม่มีคีย์นั้นส่งมา

4. พื้นฐาน API (ตัวอย่าง `/api/time`)

	- ฟังก์ชัน route ที่คืนค่า JSON ใช้ `jsonify(...)` เพื่อสร้าง `Response` ที่มี `Content-Type: application/json` อัตโนมัติ
	- ตัวอย่างใน `app.py` คืนค่าเวลาของเซิร์ฟเวอร์ (UTC) ในรูปแบบ ISO string เช่น `{ "time": "2026-04-17T12:34:56.789Z" }`
	- สามารถเรียก API นี้จากเบราว์เซอร์, `curl`, หรือ JavaScript `fetch()` เพื่อรับข้อมูลแบบโปรแกรมได้ เช่น `curl http://127.0.0.1:5000/api/time`

---



