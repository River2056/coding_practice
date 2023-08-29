def taskAssignment(k, tasks):
    copy_tasks = sorted([(k, t) for k, t in enumerate(tasks)], key=lambda x: x[1])
    left, right = 0, len(copy_tasks) - 1
    res = []

    while k > 0 and left <= right:
        task = [copy_tasks[left][0], copy_tasks[right][0]]
        if left == right:
            task = [copy_tasks[left][0]]
        left += 1
        right -= 1
        k -= 1
        res.append(task)

    return res


def main():
    k = 3
    tasks = [1, 3, 5, 3, 1, 4]

    result = taskAssignment(k, tasks)
    print(result)
    assert result == [
        [0, 2],
        [4, 5],
        [1, 3],
    ], f"expected [[0, 2], [4, 5], [1, 3]], got {result} instead"


if __name__ == "__main__":
    main()
