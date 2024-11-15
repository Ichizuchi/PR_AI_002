# Подсчет количества островов
def count_islands(matrix):
    def dfs(x, y):
        if x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]) or matrix[x][y] == 0:
            return
        matrix[x][y] = 0  
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]:
            dfs(x + dx, y + dy)
    
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                count += 1
                dfs(i, j)
    return count

custom_matrix = [
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
]
print("Количество островов:", count_islands(custom_matrix))
