def shortestDistance(words: list[str], word1: str, word2: str) -> int:
    m = {}
    m[word1] = None
    m[word2] = None
    shortest = float("inf")

    for idx, w in enumerate(words):
        if w == word1 or w == word2:
            m[w] = idx
            if m[word1] is not None and m[word2] is not None:
                d = abs(m[word1] - m[word2])
                shortest = min(shortest, d)
    return int(shortest)


def main():
    print(
        shortestDistance(
            ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"],
            "fox",
            "dog",
        )
    )  # 5
    print(shortestDistance(["a", "c", "d", "b", "a"], "a", "b"))  # 1
    print(shortestDistance(["a", "b", "c", "d", "e"], "a", "e"))  # 4


if __name__ == "__main__":
    main()
