def reverseVowels(s: str) -> str:
    left, right = 0, len(s) - 1
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    s_arr = list(s)
    while left < right:
        while s_arr[left] not in vowels:
            left += 1
        while s_arr[right] not in vowels:
            right -= 1
        if left < right:
            s_arr[left], s_arr[right] = s_arr[right], s_arr[left]
        left += 1
        right -= 1

    return "".join(s_arr)


def main():
    print(reverseVowels("hello"))  # holle
    print(reverseVowels("AEIOU"))  # UOIEA
    print(reverseVowels("DesignGUrus"))  # DusUgnGires


if __name__ == "__main__":
    main()
