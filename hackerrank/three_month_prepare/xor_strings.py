def strings_xor(s, t):
    res = []
    for i in range(len(s)):
        if s[i] == t[i]:
            res.append("0")
        else:
            res.append("1")

    return "".join(res)


def main():
    s = "10101"
    t = "00101"
    print(strings_xor(s, t))


if __name__ == "__main__":
    main()
