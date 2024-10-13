import heapq

def draw_Dijkstra(graph, start_node, target_node):
    priority_queue = []
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0  # Distance to itself is zero
    previous_nodes = {node: None for node in graph}  # To track the path
    heapq.heappush(priority_queue, (0, start_node))
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    path = reconstruct_path(previous_nodes, target_node)
    return distances[target_node], path  # Return the distance, path, and elapsed time


def draw_A_star(graph, start_node, target_node):
    priority_queue = []
    g_costs = {node: float('inf') for node in graph}
    g_costs[start_node] = 0
    previous_nodes = {node: None for node in graph}
    def heuristic(current_node, target_node):
        return 0
    heapq.heappush(priority_queue, (0 + heuristic(start_node, target_node), 0, start_node))
    while priority_queue:
        f_cost, current_g, current_node = heapq.heappop(priority_queue)
        if current_node == target_node:
            path = reconstruct_path(previous_nodes, target_node)
            return current_g, path
        for neighbor, weight in graph[current_node].items():
            tentative_g = current_g + weight
            if tentative_g < g_costs[neighbor]:
                g_costs[neighbor] = tentative_g
                f_cost = tentative_g + heuristic(neighbor, target_node)
                heapq.heappush(priority_queue, (f_cost, tentative_g, neighbor))
                previous_nodes[neighbor] = current_node
    return float('inf'), [], 0


def reconstruct_path(previous_nodes, target_node):
    path = []
    current = target_node
    while current is not None:
        path.append(current)
        current = previous_nodes[current]
    path.reverse()
    return path
