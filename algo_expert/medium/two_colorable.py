def twoColorable(edges):
    visited = set()
    colors = [None for _ in edges]
    stack = []
    stack.append((edges[0], 0))
    while len(stack) > 0:
        node = stack.pop()
        visited.add(node[1])
        res = color_nodes(colors, node[0], node[1])
        if not res:
            return False
        for edge in node[0]:
            if edge not in visited:
                stack.append((edges[edge], edge))
    return True


def color_nodes(colors, edge, index):
    if colors[index] is None:
        colors[index] = True
    for e in edge:
        if colors[e] is None:
            colors[e] = False if colors[index] is None else not colors[index]
        else:
            if colors[e] == colors[index]:
                return False
    return True


def main():
    edges = [[1, 2], [0, 2], [0, 1]]
    result = twoColorable(edges)
    assert not result, f"expected False, got {result} instead"

    edges = [[1], [0]]
    result = twoColorable(edges)
    assert result, f"expected True, got {result} instead"

    edges = [[1, 3], [0, 2], [1, 3], [0, 2]]
    result = twoColorable(edges)
    assert result, f"expected True, got {result} instead"


if __name__ == "__main__":
    main()
