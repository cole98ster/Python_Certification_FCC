def dfs(matrix, node):
    n = len(matrix)
    visited = [False]* n
    result = []
    stack = [node]

    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            result.append(current)
            for neighbor in range(n - 1, -1, -1):
                if matrix[current][neighbor] == 1 and not visited[neighbor]:
                    stack.append(neighbor)
    return result

dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 1)
