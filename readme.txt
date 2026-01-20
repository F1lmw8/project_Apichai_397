คู่มือระบบ Movie Service (System Manual)
=====================================
ระบบนี้จำลองแนวคิด Object-Oriented Programming (OOP) ผ่าน Microservices

องค์ประกอบหลัก (Architecture Components)
-------------------------------------

1. Service A (Class แม่ / Base Class)
   - ไฟล์หลัก: service_a/grpc_server.py
   - หน้าที่: เป็น "แหล่งข้อมูลหลัก" (Database) เก็บข้อมูลหนังทั้งหมด
   - เปรียบเสมือน: Base Class ใน OOP ที่มี property (ข้อมูลหนัง) และ method (get_movie)
   - การทำงาน: เปิด gRPC Server (port 50051) รอให้ลูกๆ เข้ามาขอข้อมูล

2. Service B (Class ลูก / Child Class - The Matrix)
   - ไฟล์หลัก: service_b/main.py
   - หน้าที่: เป็นตัวแทนของหนังเรื่อง "The Matrix"
   - เปรียบเสมือน: Child Class ที่ Inherit มาจาก Service A แต่ระบุตัวตนชัดเจนว่าเป็น The Matrix
   - การทำงาน:
     - เมื่อผู้ใช้เรียก /my-movie
     - Service B จะวิ่งไปขอข้อมูล ID=8 จาก Service A
     - นำข้อมูลมาแสดงผลพร้อมระบุว่า "ฉันคือ The Matrix"

3. Service C (Class ลูก / Child Class - Titanic)
   - ไฟล์หลัก: service_c/main.py
   - หน้าที่: เป็นตัวแทนของหนังเรื่อง "Titanic"
   - เปรียบเสมือน: Child Class อีกหนึ่งตัว ที่ Inherit จาก A เหมือนกัน แต่เป็นคนละ Object
   - การทำงาน:
     - เมื่อผู้ใช้เรียก /my-movie
     - Service C จะวิ่งไปขอข้อมูล ID=6 จาก Service A
     - นำข้อมูลมาแสดงผลพร้อมระบุว่า "ฉันคือ Titanic"

หลักการทำงาน (Working Principle)
------------------------------
1. Inheritance (การสืบทอด):
   - Service B และ C ไม่ได้เก็บข้อมูลหนังไว้ที่ตัวเอง
   - ทั้งคู่ "สืบทอด" ข้อมูลมาจาก Service A ผ่าน gRPC
   - ถ้า Service A แก้ไขข้อมูล Service B และ C จะได้ข้อมูลใหม่ทันที (เหมือน Class ลูกได้ property ใหม่จากแม่)

2. Polymorphism (ความหลากหลาย):
   - Endpoint เดียวกัน (/my-movie)
   - เรียกที่ Service B ได้ "The Matrix"
   - เรียกที่ Service C ได้ "Titanic"
   - แม้จะเรียกวิธีเดียวกัน แต่ผลลัพธ์ต่างกันตาม "ตัวตน" ของ Service นั้นๆ

วิธีใช้งาน (Usage Guide)
----------------------
1. เปิด Service B (The Matrix)
   - URL: http://localhost:8001/my-movie
   - ผลลัพธ์: ข้อมูลหนัง The Matrix

2. เปิด Service C (Titanic)
   - URL: http://localhost:8002/my-movie
   - ผลลัพธ์: ข้อมูลหนัง Titanic

3. ดูหนังเรื่องอื่นผ่าน Service B
   - URL: http://localhost:8001/movie/{id}
   - ตัวอย่าง: http://localhost:8001/movie/1 (Shawshank Redemption)
