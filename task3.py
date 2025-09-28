import heapq

# Функція Дейкстри
def dijkstra(graph, start):
    # Відстані до вершин
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    # Черга з пірамідою: (вартість, вершина)
    heap = [(0, start)]
    previous = {vertex: None for vertex in graph}

    while heap:
        current_dist, current_vertex = heapq.heappop(heap)  # Витягаємо вершину з min відстанню
        if current_dist > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance  # Оновлюємо відстань якщо знайшли коротший шлях
                previous[neighbor] = current_vertex
                heapq.heappush(heap, (distance, neighbor))
    return distances, previous

# Відновлює шлях з previous
def get_path(previous, start, end):
    path = []
    current = end
    while current != start:
        path.append(current)
        current = previous[current]
        if current is None:
            return []
    path.append(start)
    path.reverse()
    return path

# Приклад використання
def example():
    # Створюємо граф 
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    start = 'A'
    distances, previous = dijkstra(graph, start)

    print(f"Найкоротші відстані від '{start}':")
    for vertex in graph:
        print(f"  {vertex}: {distances[vertex]}")

    end = 'D'
    path = get_path(previous, start, end)
    print(f"\nНайкоротший шлях від '{start}' до '{end}':", ' -> '.join(path))

if __name__ == "__main__":
    example()
