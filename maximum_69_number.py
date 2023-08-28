def maximum_69_number(num):
    arr = list(str(num))
    for k, v in enumerate(arr):
        if v == "6":
            arr[k] = "9"
            return int("".join(arr))
    return num


def maximum_69_number_2(num):
    k = -1
    num_copy = num

    i = 0
    while num_copy > 0:
        r = num_copy % 10
        if r == 6:
            k = i
        num_copy //= 10
        i += 1
    return num + (3 * (10**k)) if k > -1 else num


def main():
    print(maximum_69_number_2(9669))
    print(maximum_69_number_2(9996))
    print(maximum_69_number_2(9999))


if __name__ == "__main__":
    main()
