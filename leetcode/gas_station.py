def canCompleteCircuit(gas: list[int], cost: list[int]) -> int:
    """
    self attempt: failed
    for i in range(len(gas)):
        e = gas[i]
        for j in range(i, i + len(gas) - 1):
            e -= cost[j % len(cost)]
            if e < 0:
                continue
            e += gas[(j + 1) % len(gas)]
        if i <= 0:
            i += len(gas)
        e -= cost[i - 1]
        if e == 0:
            return i
    return -1

    """
    if sum(gas) < sum(cost):
        return -1

    total = 0
    start = 0
    for i in range(len(gas)):
        total += (gas[i] - cost[i])
        if total < 0:
            total = 0
            start = i + 1

    return start


def main():
    res = canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])
    print(f"result: {res}")

    res = canCompleteCircuit([2, 3, 4], [3, 4, 3])
    print(f"result: {res}")

    res = canCompleteCircuit([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
    print(f"result: {res}")


if __name__ == "__main__":
    main()
