def search(arr: list[int], target_sum: int) -> list[int]:
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum < target_sum:
            left += 1
        elif current_sum > target_sum:
            right -= 1
        else:
            return [left, right]
    return [-1, -1]


def main():
    print(search([1, 2, 3, 4, 6], 6))  # [1, 3]
    print(search([2, 5, 9, 11], 11))  # [0, 2]
    print(search([0, 1, 2, 3, 4], 0))  # [0, 0]


if __name__ == "__main__":
    main()
