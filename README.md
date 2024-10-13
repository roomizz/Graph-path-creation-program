โปรแกรมนี้จะสร้างกราฟและหาเส้นทางที่ดีที่สุดโดยใช้ A* และ Dijkstra โดยมีแผนที่ให้เลือก 5 แบบ ไล่ตามระดับความซับซ้อน และคุณสามารถสร้างแผนที่เองได้ด้วยคำสั่ง cotton

หากคุณใช้คำสั่ง cotton เพื่อสร้างแผนที่ที่ซับซ้อนจนโปรแกรมไม่สามารถทำงานได้ ให้แก้ไขค่าของ WIDTH และ HEIGHT ในไฟล์ t.py ตามขนาดที่หน้าจอของคุณสามารถรองรับได้ (เนื่องจากฟังก์ชัน random_map จะไม่ทำงานหากค่าของ WIDTH, HEIGHT และ dis (ระยะห่างระหว่างโหนด) ไม่สมเหตุสมผล)

This program creates a graph and finds the optimal path using A* and Dijkstra. There are 5 maps to choose from, ordered by complexity, and you can also create your own map using the cotton command.

If you use the cotton command to generate a map that is too complex for the program to handle, you can adjust the WIDTH and HEIGHT values in t.py to fit the size your screen can accommodate. (The random_map function won't work if the WIDTH, HEIGHT, and dis (distance between nodes) values are not reasonable.)
