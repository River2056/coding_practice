def cycleInGraph(edges):
    visited = [False for _ in edges]
    in_stack = [False for _ in edges]

    for node in range(len(edges)):
        if visited[node]:
            continue

        contains_cycle = is_node_in_cycle(edges, node, visited, in_stack)
        if contains_cycle:
            return True

    return False

def is_node_in_cycle(edges, node, visited, in_stack):
    node_edge = edges[node]
    visited[node] = True
    in_stack[node] = True
    for ne in node_edge:
        if not visited[ne]:
            contains_cycle = is_node_in_cycle(edges, ne, visited, in_stack)
            if contains_cycle:
                return True
        elif in_stack[ne]:
            return True
    in_stack[node] = False
    return False


def main():
    edge = [[1, 3], [2, 3, 4], [0], [], [2, 5], []]
    result = cycleInGraph(edge)
    assert result, f"expected True, got {result} instead"


if __name__ == "__main__":
    main()
