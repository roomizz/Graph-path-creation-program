import random
import math
import pandas as pd

nodes = []
connections = []
node_positions = {}

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def lines_intersect(p1, p2, p3, p4):
    def ccw(a, b, c):
        return (c[1] - a[1]) * (b[0] - a[0]) > (b[1] - a[1]) * (c[0] - a[0])
    return ccw(p1, p3, p4) != ccw(p2, p3, p4) and ccw(p1, p2, p3) != ccw(p1, p2, p4)

def coo1(num_nodes, min_distance, max_distance, max_connections):
    local_connections = []
    for i in range(num_nodes):
        distances = []
        for j in range(num_nodes):
            if i != j:
                dist = distance(node_positions[i], node_positions[j])
                road = random.randint(min_distance, max_distance)
                distances.append((dist, j, road))
        distances.sort()
        closest_nodes = distances[:max_connections]
        for _, j, road1 in closest_nodes:
            can_connect = True
            for k in local_connections:
                if lines_intersect(
                        node_positions[i], node_positions[j],
                        node_positions[k[0]], node_positions[k[1]]):
                    can_connect = False
                    break
            if can_connect:
                local_connections.append((i, j, road1))
    return local_connections

def coo(WIDTH, HEIGHT, num_nodes,dis):
    local_nodes = []
    while len(local_nodes) < num_nodes:
        x = random.randint(-WIDTH // 2, WIDTH // 2)
        y = random.randint(-HEIGHT // 2, HEIGHT // 2)
        new_node = (len(local_nodes), f"Node {len(local_nodes) + 1}", x, y)
        if all(distance((x, y), (node[2], node[3])) >= dis for node in local_nodes):
            local_nodes.append(new_node)
            node_positions[len(local_nodes) - 1] = (x, y)
    return local_nodes

def coo2(num_nodes, min_distance, max_distance):
    local_connections = []
    for i in range(num_nodes):
        if not any(i in conn for conn in connections):
            while True:
                j = random.randint(0, num_nodes - 1)
                if j != i:
                    local_connections.append((i, j, random.randint(min_distance, max_distance)))  # เพิ่ม random road1 ด้วย
                    break
    return local_connections

def random_map(WIDTH, HEIGHT, min_distance, max_distance, num_nodes, dis, max_connections):
    # สร้างโหนดและการเชื่อมต่อ
    global nodes, connections
    nodes = coo(WIDTH, HEIGHT, num_nodes,dis)
    connections = coo1(num_nodes, min_distance, max_distance, max_connections)
    connections += coo2(num_nodes, min_distance, max_distance)
    nodes_df = pd.DataFrame(nodes, columns=['id', 'name', 'x', 'y'])
    nodes_df.to_csv('road_random/nodes.csv', index=False)
    connections_df = pd.DataFrame(connections, columns=['source', 'destination', 'road'])
    connections_df.to_csv('road_random/connections.csv', index=False)
