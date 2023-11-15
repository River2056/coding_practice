def migratoryBirds(arr):
    seen = {}
    for bird in arr:
        if bird not in seen:
            seen[bird] = 1
        else:
            seen[bird] += 1

    most_seen = max(seen.values())
    most_sighted = list(filter(lambda x: x[1] == most_seen, seen.items()))
    return min([item[0] for item in most_sighted])


def main():
    print(migratoryBirds([1, 1, 2, 2, 3]))  # 1


if __name__ == "__main__":
    main()
