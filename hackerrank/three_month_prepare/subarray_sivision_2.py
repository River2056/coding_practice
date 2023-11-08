def birthday(s: list[int], d: int, m: int) -> int:
    total = 0
    for i in range(len(s) - m + 1):
        if sum(s[i : i + m]) == d:
            total += 1

    return total


def main():
    print(birthday([2, 2, 1, 3, 2], 4, 2))  # prints 2, since 2 combinations
    print(birthday([1, 1, 1, 1, 1, 1], 3, 2))  # 0
    print(birthday([4], 4, 1))  # 1


if __name__ == "__main__":
    main()
