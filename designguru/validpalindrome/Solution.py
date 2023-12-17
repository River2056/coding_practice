def isPalindrome(s: str) -> bool:
    s = s.lower()
    arr = list(filter(lambda x: x.isalnum(), list(s)))
    if len(arr) == 0:
        return False

    left, right = 0, len(arr) - 1
    while left <= right:
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1
    return True


def main():
    print(isPalindrome("A man, a plan, a canal, Panama!"))  # True
    print(isPalindrome("Was it a car or a cat I saw?"))  # True
    print(isPalindrome("12345"))  # False
    print(isPalindrome("12321"))  # True


if __name__ == "__main__":
    main()
