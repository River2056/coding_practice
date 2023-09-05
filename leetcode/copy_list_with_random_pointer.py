class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __str__(self):
        return f"{{ val: {self.val} }}"


def copyRandomList(head: Node) -> Node:
    copy_nodes = []
    items = {}
    current = head
    while current is not None:
        copy_nodes.append(Node(current.val))
        current = current.next

    i = 0
    current = head
    while current is not None:
        items[current] = i
        current = current.next
        i += 1

    i = 0
    current = head
    while current is not None:
        next_node = current.next
        next_random = current.random
        if next_node is not None:
            next_index = items[next_node]
            copy_nodes[i].next = copy_nodes[next_index]

        if next_random is not None:
            next_random_index = items[next_random]
            copy_nodes[i].random = copy_nodes[next_random_index]

        current = current.next
        i += 1

    return copy_nodes[0]


def printList(head):
    current = head
    while current is not None:
        print(current)
        print(f"next: {current.next}")
        print(f"random: {current.random}")
        print()
        current = current.next


def main():
    head = Node(7)
    a = Node(13)
    b = Node(11)
    c = Node(10)
    d = Node(1)

    head.next = a
    a.next = b
    b.next = c
    c.next = d

    a.random = head
    b.random = d
    c.random = b
    d.random = head

    # printList(head)
    new_head = copyRandomList(head)
    printList(new_head)


if __name__ == "__main__":
    main()
