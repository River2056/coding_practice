def sortArray(nums: list[int]) -> list[int]:
    print("before sort: ", nums)
    nums = merge_sort(nums)
    print("after sort: ", nums)

    return nums


def merge_sort(nums: list[int]) -> list[int]:
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = merge_sort(nums[0:mid])
    right = merge_sort(nums[mid:len(nums)])

    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    while i < len(left):
        res.append(left[i])
        i += 1

    while j < len(right):
        res.append(right[j])
        j += 1

    return res


def quick_sort(nums: list[int], start: int, end: int):
    """
    first try, wasn't correct
    forgot about the worst time complexity XD
    """
    if start >= end:
        return
    pivot = end
    i = start - 1
    j = start

    while j < end:
        if nums[j] < nums[pivot]:
            i += 1
            tmp = nums[j]
            nums[j] = nums[i]
            nums[i] = tmp
        j += 1
    i += 1

    tmp = nums[pivot]
    nums[pivot] = nums[i]
    nums[i] = tmp

    quick_sort(nums, start, i - 1)
    quick_sort(nums, i + 1, end)


def main():
    arr = [5, 2, 3, 1]
    print(sortArray(arr))  # 1, 2, 3, 5


if __name__ == "__main__":
    main()
