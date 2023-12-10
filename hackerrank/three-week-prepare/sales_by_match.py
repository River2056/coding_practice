def sockMerchant(n, ar):
    pairs = 0
    seen = set()
    for sock in ar:
        if sock not in seen:
            seen.add(sock)
        else:
            seen.remove(sock)
            pairs += 1
    return pairs


def main():
    print(sockMerchant(7, [1, 2, 1, 2, 1, 3, 2]))  # 2, 2 pairs of socks
    print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])) # 3


if __name__ == "__main__":
    main()
