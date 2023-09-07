def letterCombinations(digits: str) -> list[str]:
    res = []
    mapping = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def backtrack(i, cur_str):
        if len(cur_str) == len(digits):
            res.append(cur_str)
            return
        for c in mapping[digits[i]]:
            backtrack(i + 1, c + cur_str)

    if digits:
        backtrack(0, "")

    return res


def main():
    result = letterCombinations("2")
    print(result)

    result = letterCombinations("23")
    print(f"result: {result}")


if __name__ == "__main__":
    main()
