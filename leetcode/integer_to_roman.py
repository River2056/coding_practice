mapping = [
    ("M", 1000),
    ("CM", 900),
    ("D", 500),
    ("CD", 400),
    ("C", 100),
    ("XC", 90),
    ("L", 50),
    ("XL", 40),
    ("X", 10),
    ("IX", 9),
    ("V", 5),
    ("IV", 4),
    ("I", 1),
]


def intToRoman(num: int) -> str:
    mapping = [
        ("M", 1000),
        ("CM", 900),
        ("D", 500),
        ("CD", 400),
        ("C", 100),
        ("XC", 90),
        ("L", 50),
        ("XL", 40),
        ("X", 10),
        ("IX", 9),
        ("V", 5),
        ("IV", 4),
        ("I", 1),
    ]
    i = 0
    res = []
    while num > 0:
        pair = mapping[i]
        repr_str = pair[0]
        repr_num = pair[1]
        if num >= repr_num:
            num -= repr_num
            res.append(repr_str)
        else:
            i += 1

    return "".join(res)


def main():
    print(mapping)
    res = intToRoman(3)
    print(res, "III", 3)  # III

    res = intToRoman(58)
    print(res, "LVIII", 58)  # LVIII

    res = intToRoman(1994)
    print(res, "MCMXCIV", 1994)  # MCMXCIV


if __name__ == "__main__":
    main()
