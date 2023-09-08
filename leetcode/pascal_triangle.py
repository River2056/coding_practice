def generate(numRows: int) -> list[list[int]]:
    res = []
    for i in range(numRows):
        arr = [None] * (i + 1)
        arr[0] = 1  # type: ignore
        arr[len(arr) - 1] = 1  # type: ignore
        for j in range(1, len(arr) - 1, 1):
            arr[j] = res[i - 1][j] + res[i - 1][j - 1]
        res.append(arr)
    return res




def main():
    print(generate(5))
    print(generate(1))


if __name__ == "__main__":
    main()
