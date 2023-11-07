import random


def findKthLargest(nums: list[int], k: int) -> int:
    def partition(start, end):
        p_idx = random.randint(start, end)
        pivot = nums[p_idx]

        tmp = nums[end]
        nums[end] = pivot
        nums[p_idx] = tmp

        pindex = start

        for i in range(start, end + 1):
            if nums[i] > pivot:
                tmp = nums[pindex]
                nums[pindex] = nums[i]
                nums[i] = tmp
                pindex += 1

        tmp = nums[end]
        nums[end] = nums[pindex]
        nums[pindex] = tmp
        return pindex

    def quick_select(start, end):
        if start <= end:
            pindex = partition(start, end)

            if pindex > k - 1:
                return quick_select(start, pindex - 1)
            elif pindex < k - 1:
                return quick_select(pindex + 1, end)
            else:
                return nums[k - 1]

    return quick_select(0, len(nums) - 1) # type: ignore

    return 0

    # def quick_select(start, end):
    #     """
    #     first try, TLE
    #     """
    #     pivot = end
    #     i, j = start - 1, start
    #     while j < end:
    #         if nums[j] >= nums[pivot]:
    #             i += 1
    #             tmp = nums[j]
    #             nums[j] = nums[i]
    #             nums[i] = tmp
    #         j += 1
    #     i += 1

    #     tmp = nums[pivot]
    #     nums[pivot] = nums[i]
    #     nums[i] = tmp

    #     if i < k - 1:
    #         return quick_select(i + 1, end)
    #     elif i > k - 1:
    #         return quick_select(start, i - 1)
    #     else:
    #         return nums[k - 1]

    # return quick_select(0, len(nums) - 1)  # type: ignore


def main():
    print(findKthLargest([3, 2, 1, 5, 6, 4], 2))  # 5
    print(findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4
    print(findKthLargest([3, 1, 2, 4], 2))  # 3
    print(findKthLargest([1], 1))  # 1


if __name__ == "__main__":
    main()
