def twoSum(nums: list[int], target: int) -> list[int]:
    cache = {}
    for k, v in enumerate(nums):
        if v in cache:
            return [cache[v], k]
        diff = target - v
        cache[diff] = k
    return []


def main():
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(nums, target))  # [0, 1]

    nums = [3, 2, 4]
    target = 6
    print(twoSum(nums, target))  # [1, 2]

    nums = [3, 3]
    target = 6
    print(twoSum(nums, target))  # [0, 1]


if __name__ == "__main__":
    main()
