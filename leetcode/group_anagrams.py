def groupAnagrams(strs: list[str]) -> list[list[str]]:
    cache = {}
    for s in strs:
        ss = "".join(sorted(list(s)))
        if ss not in cache:
            cache[ss] = [s]
        else:
            cache[ss].append(s)

    return cache.values() # type: ignore


def main():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(strs))  # [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

    strs = [""]
    print(groupAnagrams(strs))  # [[""]]

    strs = ["a"]
    print(groupAnagrams(strs))  # [["a"]]


if __name__ == "__main__":
    main()
