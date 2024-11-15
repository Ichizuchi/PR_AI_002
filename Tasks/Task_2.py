# Поиск кратчайшего пути
from collections import deque

def shortest_path(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(start, 0)])
    visited = set()
    
    while queue:
        (x, y), distance = queue.popleft()
        if (x, y) == goal:
            return distance
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 1 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), distance + 1))
    return -1

# Пример использования
custom_maze = [
    [1, 1, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 1, 1],
    [0, 0, 0, 1]
]
start_position = (0, 0)
goal_position = (3, 3)
print("Длина кратчайшего пути:", shortest_path(custom_maze, start_position, goal_position))
