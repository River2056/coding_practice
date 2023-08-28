def removeIslands(matrix):
    visited = [[False] * len(arr) for arr in matrix]

    def dfs(x, y, is_edge):
        if y >= len(matrix) or y < 0:
            return
        arr = matrix[y]
        if x >= len(arr) or x < 0:
            return
        if visited[y][x]:
            return

        visited[y][x] = True
        if matrix[y][x] == 0:
            return
        if not is_edge and matrix[y][x] == 1:
            matrix[y][x] = 0
        dfs(x - 1, y, is_edge)
        dfs(x + 1, y, is_edge)
        dfs(x, y - 1, is_edge)
        dfs(x, y + 1, is_edge)

    for i in range(len(matrix[0])):
        dfs(i, 0, True)
    for i in range(len(matrix[len(matrix) - 1])):
        dfs(i, len(matrix) - 1, True)
    for i in range(len(matrix)):
        dfs(len(matrix[i]) - 1, i, True)
    for i in range(len(matrix)):
        dfs(0, i, True)

    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            dfs(x, y, False)

    return matrix


def main():
    """
    [
      [1, 0, 0, 0, 0, 0],
      [0, 0, 0, 1, 1, 1],
      [0, 0, 0, 0, 1, 0],
      [1, 1, 0, 0, 1, 0],
      [1, 0, 0, 0, 0, 0],
      [1, 0, 0, 0, 0, 1],
    ]
    """
    # result = removeIslands(
    #     [
    #         [1, 0, 0, 0, 0, 0],
    #         [0, 1, 0, 1, 1, 1],
    #         [0, 0, 1, 0, 1, 0],
    #         [1, 1, 0, 0, 1, 0],
    #         [1, 0, 1, 1, 0, 0],
    #         [1, 0, 0, 0, 0, 1],
    #     ]
    # )

    # for arr in result:
    #     print(arr)

    result = removeIslands(
        [
            [1, 0, 0, 0, 1, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [1, 1, 0, 1, 0, 0, 1, 0],
            [1, 1, 0, 1, 1, 0, 1, 0],
            [1, 0, 0, 0, 1, 0, 0, 0],
        ]
    )

    for arr in result:
        print(arr)


if __name__ == "__main__":
    main()
