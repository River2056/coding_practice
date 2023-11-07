def topKFrequent(nums: list[int], k: int) -> list[int]:
    cache = {}
    for num in nums:
        if num not in cache:
            cache[num] = 1
        else:
            cache[num] += 1
    freq = sorted([entry for entry in cache.items()], key=lambda x: x[1], reverse=True)
    freq = list(map(lambda x: x[0], freq))
    res = [freq.pop(0) for _ in range(k)]
    return res


def main():
    arr = [1, 1, 1, 2, 2, 3]
    print(topKFrequent(arr, 2))  # [1, 2]

    arr = [1]
    print(topKFrequent(arr, 1))  # [1]


if __name__ == "__main__":
    main()
