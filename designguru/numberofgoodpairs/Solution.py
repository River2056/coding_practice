def numGoodPairs(nums: list[int]) -> int:
    seen = {}
    pair_count = 0
    for n in nums:
        if n not in seen:
            seen[n] = 1
        else:
            seen[n] += 1
        pair_count = seen[n] - 1 + pair_count
    return pair_count


def main():
    print(numGoodPairs([1, 2, 3, 1, 1, 3]))  # 4
    print(numGoodPairs([1, 1, 1, 1]))  # 6
    print(numGoodPairs([1, 2, 3]))  # 0


if __name__ == "__main__":
    main()
