def remove(arr: list[int]) -> int:
    count = 1

    if len(arr) == 0:
        return 0

    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            count += 1

    return count


def main():
    print(remove([2, 3, 3, 3, 6, 9]))  # 4
    print(remove([2, 2, 2, 11]))  # 2


if __name__ == "__main__":
    main()
