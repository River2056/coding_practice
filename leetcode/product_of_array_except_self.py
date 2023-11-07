def productExceptSelf(nums: list[int]) -> list[int]:
    res = []
    prod = 1
    for i in range(len(nums)):
        res.append(prod)
        prod *= nums[i]

    prod = 1
    for i in range(len(res) - 1, -1, -1):
        res[i] *= prod
        prod *= nums[i]

    return res


def main():
    print(productExceptSelf([1, 2, 3, 4]))  # [24, 12, 8, 6]
    print(productExceptSelf([-1, 1, 0, -3, 3]))  # [0, 0, 9, 0, 0]


if __name__ == "__main__":
    main()
