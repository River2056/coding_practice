def two_arrays(k: int, A: list[int], B: list[int]):
    a_sort = sorted(A)
    b_sort = sorted(B, reverse=True)
    for a, b in zip(a_sort, b_sort):
        if a + b < k:
            return "NO"
    return "YES"


def main():
    print(two_arrays(4, [1, 3], [3, 1]))
    print(two_arrays(5, [2, 3, 1, 1, 1], [1, 3, 4, 3, 3]))
    print(two_arrays(9, [1, 5, 1, 4, 4, 2, 7, 1, 2, 2], [8, 7, 1, 7, 7, 4, 4, 3, 6, 7]))
    print(two_arrays(9, [3, 6, 8, 5, 9, 9, 4, 8, 4, 7], [5, 1, 0, 1, 6, 4, 1, 7, 4, 3]))
    print(two_arrays(4, [4, 4, 3, 2, 1, 4, 4, 3, 2, 4], [2, 3, 0, 1, 1, 3, 1, 0, 0, 2]))


def test():
    cache = {1: 2, 2: 3, 3: 5, 6: 1}
    for item in cache.items():
        print(item)


if __name__ == "__main__":
    # test()
    main()
