def riverSizes(matrix):
    res = []
    visited = [[False] * len(arr) for arr in matrix]

    def dfs(x, y, count):
        if y >= len(matrix) or y < 0:
            return
        arr = matrix[y]
        if x >= len(arr) or x < 0:
            return

        if matrix[y][x] == 0 or visited[y][x]:
            return

        if matrix[y][x] == 1:
            visited[y][x] = True
            count[0] += 1
        dfs(x + 1, y, count)
        dfs(x - 1, y, count)
        dfs(x, y + 1, count)
        dfs(x, y - 1, count)

    for y, _ in enumerate(matrix):
        for x, _ in enumerate(matrix[y]):
            count = [0]
            dfs(x, y, count)
            if count[0] > 0:
                res.append(count[0])
    return res


def main():
    result = riverSizes(
        [
            [1, 0, 0, 1, 0],
            [1, 0, 1, 0, 0],
            [0, 0, 1, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 0],
        ]
    )
    print(result)  # [1, 2, 2, 2, 5] in any order


if __name__ == "__main__":
    main()
