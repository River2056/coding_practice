def subsets_self(nums: list[int]) -> list[list[int]]:
    res = []

    def backtrack(index, sub):
        if index >= len(nums) and sub not in res:
            res.append([e for e in sub])
            return
        for i in range(index, len(nums)):
            sub.append(nums[i])
            backtrack(i + 1, sub)
            if sub:
                sub.pop()
            backtrack(i + 1, sub)

    backtrack(0, [])
    return res


def subsets(nums: list[int]) -> list[list[int]]:
    res = []

    cur = []

    def dfs(i):
        if i >= len(nums):
            res.append([e for e in cur])
            return
        cur.append(nums[i])
        dfs(i + 1)
        cur.pop()
        dfs(i + 1)
    dfs(0)

    return res


def main():
    result = subsets([1, 2, 3])
    print(result)

    result = subsets([0])
    print(result)


if __name__ == "__main__":
    main()
