def minimumPassesOfMatrix(matrix):
    passes = 0
    copy_grid = [[i for i in arr] for arr in matrix]
    while True:
        for y, _ in enumerate(copy_grid):
            for x, _ in enumerate(copy_grid[y]):
                if copy_grid[y][x] != 0 and copy_grid[y][x] < 0:
                    positive_neighbors = 0
                    positive_neighbors += check_neighbor(matrix, x + 1, y)
                    positive_neighbors += check_neighbor(matrix, x - 1, y)
                    positive_neighbors += check_neighbor(matrix, x, y + 1)
                    positive_neighbors += check_neighbor(matrix, x, y - 1)
                    if positive_neighbors > 0:
                        copy_grid[y][x] = abs(copy_grid[y][x])
        if copy_grid != matrix:
            passes += 1
            matrix = [[i for i in arr] for arr in copy_grid]
        else:
            for arr in matrix:
                negatives = len(list(filter(lambda x: x > 0, arr)))
                if negatives > 0:
                    return -1
            return passes if passes > 0 else -1


def check_neighbor(grid, x, y):
    if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[y]):
        return 0
    if grid[y][x] > 0:
        return 1
    return 0


def main():
    matrix = [[0, -2, -2], [-5, 2, 0], [-6, -2, 0]]
    passes = minimumPassesOfMatrix(matrix)
    print(passes)
    print(matrix)
    assert passes == 2


def test():
    m = [[1, 2, 3], [2, 3, 4]]
    n = [[i for i in a] for a in m]
    n[0][0] = 0
    print(m)
    print(n)


if __name__ == "__main__":
    main()
