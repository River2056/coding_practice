def isAnagram(s: str, t: str) -> bool:
    cache = {}
    for _, v in enumerate(s):
        if v not in cache:
            cache[v] = 1
        else:
            cache[v] += 1

    for _, v in enumerate(t):
        if v not in cache:
            return False
        else:
            cache[v] -= 1
    return len(list(filter(lambda x: x != 0, cache.values()))) == 0  # type: ignore


def main():
    print(isAnagram("anagram", "nagaram"))  # True
    print(isAnagram("rat", "car"))  # False


if __name__ == "__main__":
    main()
