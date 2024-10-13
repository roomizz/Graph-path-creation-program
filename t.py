from tkinter import *
import turtle
import pandas as pd
import my_module
import A_road
import time

WIDTH = 1100
HEIGHT = 600
a = 0
nodes = []
connections = []

def setup_turtle_in_canvas(canvas):
    screen = turtle.TurtleScreen(canvas)
    screen.bgcolor("white")

    node_turtle = turtle.RawTurtle(screen)
    node_turtle.speed(0)
    node_turtle.hideturtle()

    path_turtle = turtle.RawTurtle(screen)
    path_turtle.speed(0)
    path_turtle.hideturtle()

    screen.tracer(0, 0)

    return node_turtle, path_turtle, screen

def draw_map(t, num):
    t.clear()  #
    screen = t.getscreen()
    screen.tracer(0)
    main_read(num)
    for node in nodes:
        x, y = node[2], node[3]
        t.penup()
        t.goto(x, y)
        t.dot(5, "black")  # วาดโหนด
        t.write(node[1], align="center", font=("Arial", 7, "normal"))
    for connection in connections:
        source_node = nodes[connection[0]]
        destination_node = nodes[connection[1]]
        road_node = connection[2]
        t.penup()
        t.goto(source_node[2], source_node[3])
        t.pendown()
        t.goto(destination_node[2], destination_node[3])
        mid_x = (source_node[2] + destination_node[2]) / 2
        mid_y = (source_node[3] + destination_node[3]) / 2
        t.penup()
        t.goto(mid_x, mid_y)
        t.write(str(road_node), align="center", font=("Arial", 6, "normal"))
    t.hideturtle()
    screen.update()

def random_x(t, form_frame, min_distance_entry, max_distance_entry, num_nodes_entry, distance_between_nodes_entry, max_connections_entry):
    min_distance = int(min_distance_entry.get())
    max_distance = int(max_distance_entry.get())
    num_nodes = int(num_nodes_entry.get())
    distance_between_nodes = int(distance_between_nodes_entry.get())
    max_connections = int(max_connections_entry.get())
    my_module.random_map(WIDTH, HEIGHT, min_distance, max_distance, num_nodes, distance_between_nodes, max_connections)
    form_frame.pack_forget()
    draw_map(t, 'road_random')

def main_read(num):
    global nodes, connections
    nodes.clear()
    connections.clear()

    nodes_df = pd.read_csv(f'{num}/nodes.csv')
    for index, row in nodes_df.iterrows():
        node_id = int(row['id'])
        name = row['name']
        x = int(row['x'])
        y = int(row['y'])
        nodes.append((node_id, name, x, y))

    connections_df = pd.read_csv(f'{num}/connections.csv')
    for index, row in connections_df.iterrows():
        source = int(row['source'])
        destination = int(row['destination'])
        road = int(row['road'])
        connections.append((source, destination, road))

def list_to_graph(edges):
    graph = {}
    for edge in edges:
        node1, node2, weight = edge
        node1 = f'Node {node1 + 1}'
        node2 = f'Node {node2 + 1}'

        if node1 not in graph:
            graph[node1] = {}
        if node2 not in graph:
            graph[node2] = {}

        graph[node1][node2] = weight
        graph[node2][node1] = weight
    return graph

def on_confirm1(path_turtle, start_entry, target_entry, result_label, road_var):
    selected_map = road_var.get()
    print(selected_map)
    if selected_map == "Dijkstra":
        x(path_turtle, start_entry, target_entry, result_label)
    elif selected_map == "A*":
        y(path_turtle, start_entry, target_entry, result_label)
    else:
        print("ยังไม่ได้เลือก")
def on_confirm(map_var, t, form_frame):
    selected_map = map_var.get()
    global nodes, connections, a
    nodes = []
    connections = []
    t.reset()
    if selected_map in ["map 1", "map 2", "map 3", "map 4", "map 5"]:
        form_frame.pack_forget()
        draw_map(t, int(selected_map[-1]))
        a = int(selected_map[-1])

    elif selected_map == "cotton":
        form_frame.pack(side=TOP, pady=10)
        a = 'cottton'
    else:
        print(f"คุณเลือก {selected_map}, แต่ไม่มีการสร้างหน้าต่าง")

def draw_path(p_t, path, clear_old=True):
    global a
    if clear_old:
        p_t.clear()
    if not path or len(path) < 2:
        print("No path to draw.")
        return
    start_node_name = path[0]
    start_node = next((node for node in nodes if node[1] == start_node_name), None)
    if start_node is not None:
        p_t.penup()
        p_t.goto(start_node[2], start_node[3])
        p_t.dot(20, "red")
    p_t.pensize(3)
    p_t.color("blue")
    for node_name in path[1:]:
        node = next((node for node in nodes if node[1] == node_name), None)
        if node is None:
            print(f"Node {node_name} not found!")
            continue
        p_t.pendown()
        p_t.goto(node[2], node[3])
        p_t.dot(10, "blue")
        if node_name == path[-1]:
            p_t.dot(20, "green")
    p_t.penup()

def x(path_turtle, start_entry, target_entry, result_label):
    start_time = time.time()
    distance, path = A_road.draw_Dijkstra(list_to_graph(connections), start_entry.get(), target_entry.get())
    end_time = time.time()
    elapsed_time = end_time - start_time
    result_text = f"ระยะทาง คือ {distance}\n"
    result_text += f"time{elapsed_time:.10f} s"
    draw_path(path_turtle, path)
    result_label.config(text=result_text)
    print(f"เส้นทาง{path}")
    print(f"ค่าDictionary{list_to_graph(connections)}")
def y(path_turtle, start_entry, target_entry, result_label):
    start_time = time.time()
    distance, path = A_road.draw_A_star(list_to_graph(connections), start_entry.get(), target_entry.get())
    end_time = time.time()
    elapsed_time = end_time - start_time
    result_text = f"ระยะทาง คือ {distance}\n"
    result_text += f"time{elapsed_time:.10f} s"
    draw_path(path_turtle, path)
    result_label.config(text=result_text)
    print(f"เส้นทาง{path}")
    print(f"ค่าDictionary{list_to_graph(connections)}")

def interface_map():
    root = Tk()
    root.title("MAP")
    root.geometry("1275x600")
    graph_frame = Frame(root)
    graph_frame.pack(side=LEFT, padx=(10, 0), fill=BOTH, expand=True)
    canvas = Canvas(graph_frame, width=WIDTH + 50, height=HEIGHT + 50)
    canvas.pack(fill=BOTH, expand=True)
    t, path_turtle, screen = setup_turtle_in_canvas(canvas)

    control_frame = Frame(root)
    control_frame.pack(side=TOP, padx=10)
    map_var = StringVar(root)
    map_var.set("map")
    map_options = ["map 1", "map 2", "map 3", "map 4", "map 5", "cotton"]
    map_menu = OptionMenu(control_frame, map_var, *map_options)
    map_menu.pack(side=TOP, padx=10, pady=(10, 0))  # เมนูอยู่ด้านบน
    button1 = Button(control_frame, text='ยืนยัน', command=lambda: on_confirm(map_var, t, form_frame))
    button1.pack(side=TOP, padx=10, pady=5)  # ปุ่มอยู่ด้านล่าง

    form_frame = Frame(control_frame)
    Label(form_frame, text="ระยะทางขั้นต่ำ:").pack()
    min_distance_entry = Entry(form_frame)
    min_distance_entry.pack()
    Label(form_frame, text="ระยะทางไม่เกิน:").pack()
    max_distance_entry = Entry(form_frame)
    max_distance_entry.pack()
    Label(form_frame, text="จำนวนโหนด:").pack()
    num_nodes_entry = Entry(form_frame)
    num_nodes_entry.pack()
    Label(form_frame, text="ระยะห่างระหว่างโหนด:").pack()
    distance_between_nodes_entry = Entry(form_frame)
    distance_between_nodes_entry.pack()
    Label(form_frame, text="จำนวนสูงสุดที่แต่ละโหนดเชื่อมได้:").pack()
    max_connections_entry = Entry(form_frame)
    max_connections_entry.pack()
    submit_button = Button(form_frame, text="ยืนยัน",
                           command=lambda: random_x(t, form_frame, min_distance_entry, max_distance_entry, num_nodes_entry,
                                                         distance_between_nodes_entry, max_connections_entry))
    submit_button.pack()

    search_frame = Frame(root)
    search_frame.pack(side=TOP, padx=10, pady=(10, 0))
    Label(search_frame, text="จุดเริ่มต้น").pack()
    start_entry = Entry(search_frame)
    start_entry.pack()
    Label(search_frame, text="เป้าหมาย").pack()
    target_entry = Entry(search_frame)
    target_entry.pack()
    road_var = StringVar(root)
    road_var.set("algorithm")
    road_options = ["Dijkstra", "A*"]
    road_menu = OptionMenu(search_frame, road_var, *road_options)
    road_menu.pack(side=TOP, padx=10, pady=(10, 0))
    result_label = Label(root, text="")
    result_label.pack(side=TOP, padx=10, pady=10)
    search_button = Button(search_frame, text="ยืนยัน",
                           command=lambda: on_confirm1(path_turtle, start_entry, target_entry, result_label, road_var))
    search_button.pack(side=TOP, padx=10, pady=5)
    root.mainloop()

if __name__ == '__main__':
    interface_map()
