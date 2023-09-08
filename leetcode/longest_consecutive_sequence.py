def longestConsecutive(nums: list[int]) -> int:
    cache = set(nums)

    max_consecutive = 0
    for num in nums:
        if num - 1 not in cache:
            count = 0
            while num in cache:
                count += 1
                num += 1
            max_consecutive = max(max_consecutive, count)

    return max_consecutive


def main():
    arr = [100, 4, 200, 1, 3, 2]
    print(longestConsecutive(arr))  # 4

    arr = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(longestConsecutive(arr))  # 9


if __name__ == "__main__":
    main()
