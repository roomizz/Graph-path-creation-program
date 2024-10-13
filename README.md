โปรแกรมนี้จะสร้างกราฟและหาเส้นทางที่ดีที่สุดด้วยA*และDijkstra โดยมีmapให้เลือก 5 แบบไล่ตามระดับความซับซ้อน และสามารถcotton map เองได้
-หากใช้คำสั่งcottonสร้างmapที่ซับซ้อนมากจนโปรแกรมเกิดใช้งานไม่ได้ ให้ไปแก้ค่าWIDTH, HEIGHT ที่ t.py ตามขนาดที่จอของคุณรับได้ 
(เนื่องจากdef random_map จะไม่ทำงานถ้าค่าWIDTH, HEIGHT กับค่าdis(ระยะห่างระหว่างNode) ไม่สมเหตุสมผล)
This program will create a graph and find the best path using A* and Dijkstra. There are 5 maps to choose from in order of complexity. You can also cotton map yourself.
- If you use the cotton command to create a map that is too complicated for the program to work, change the WIDTH, HEIGHT values ​​in t.py to the size that your screen can handle.
(Because def random_map will not work if the WIDTH, HEIGHT and dis values ​​(distance between nodes) are not reasonable.)
