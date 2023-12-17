def checkIfPangram(sentence: str):
    sentence = sentence.lower()
    s = set()
    for c in sentence:
        if c.isalpha():
            s.add(c)
    return len(s) == 26


def main():
    pass


if __name__ == "__main__":
    main()
