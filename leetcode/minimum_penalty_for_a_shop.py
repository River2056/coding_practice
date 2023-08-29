def bestClosingTimeSelf(customers: str) -> int:
    earliest_hour = 0
    y = 0
    for c in customers:
        if c == "Y":
            y += 1

    minimum_penalty = current_penalty = y
    for k, c in enumerate(customers):
        if c == "Y":
            current_penalty -= 1
        else:
            current_penalty += 1
        if current_penalty < minimum_penalty:
            minimum_penalty = current_penalty
            earliest_hour = k + 1

    return earliest_hour


def bestClosingTime(customers: str) -> int:
    length = len(customers)
    prefix_n = [0] * (length + 1)
    postfix_y = [0] * (length + 1)

    for i in range(1, length + 1):
        prefix_n[i] = prefix_n[i - 1] + (
            1 if i < length and customers[i - 1] == "N" else 0
        )
    print(prefix_n)
    for i in range(length - 1, -1, -1):
        postfix_y[i] = postfix_y[i + 1] + (1 if i >= 0 and customers[i] == "Y" else 0)
    print(postfix_y)

    minimum = length
    early = 0
    for i in range(length + 1):
        r = prefix_n[i] + postfix_y[i]
        if r < minimum:
            minimum = r
            early = i
    return early


def main():
    log = "YYNY"
    result = bestClosingTime(log)
    assert result == 2, f"expected 2, got {result} instead"

    log = "YYYY"
    result = bestClosingTime(log)
    assert result == 4, f"expected 4, got {result} instead"


if __name__ == "__main__":
    main()
