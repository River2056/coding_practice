def isAnagram(s: str, t: str) -> bool:
    seen = {}
    for c in s:
        if c not in seen:
            seen[c] = 1
        else:
            seen[c] += 1

    for c in t:
        if c in seen:
            seen[c] -= 1
        else:
            seen[c] = 0
            seen[c] -= 1
    return len(list(filter(lambda x: x != 0, list(seen.values())))) == 0


def main():
    print(isAnagram("listen", "silent"))  # True
    print(isAnagram("rat", "car"))  # False
    print(isAnagram("hello", "world"))  # False


if __name__ == "__main__":
    main()
