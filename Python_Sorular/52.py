# Bir grafikteki en kısa yol algoritmasını (Dijkstra, A*) Python kullanarak nasıl uygulayabilirsiniz?

import heapq

def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        if current_distance > distances[current_node]:
            continue
        
        if current_node == end:
            break
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    
    return distances[end]

# Örnek kullanım
graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'A': 2, 'C': 1, 'D': 3},
    'C': {'A': 4, 'B': 1, 'D': 2},
    'D': {'B': 3, 'C': 2}
}

start_node = 'A'
end_node = 'D'

shortest_distance = dijkstra(graph, start_node, end_node)
print("En kısa mesafe:", shortest_distance)
