def maximumPerimeterTriangle(sticks):
    sticks.sort()
    max_triangle = [-1, -1, -1]

    for i in range(len(sticks) - 2):
        a, b, c = sticks[i], sticks[i + 1], sticks[i + 2]
        if a + b > c and a + b + c > sum(max_triangle):
            max_triangle = [a, b, c]

    if sum(max_triangle) <= 0:
        return [-1]

    return max_triangle


def main():
    print(maximumPerimeterTriangle([1, 2, 3, 4, 5, 10]))  # (3, 4, 5)
    print(maximumPerimeterTriangle([1, 1, 1, 3, 3]))  # (1, 3, 3)


if __name__ == "__main__":
    main()
