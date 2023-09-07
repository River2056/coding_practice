class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween(head, left, right):
    dummy = ListNode(0, head)

    left_prev, cur = dummy, head
    for _ in range(left - 1):
        left_prev, cur = cur, cur.next

    prev = None
    for _ in range(right - left + 1):
        next_node = cur.next
        cur.next = prev
        prev, cur = cur, next_node
    left_prev.next.next = cur  # type: ignore
    left_prev.next = prev
    return dummy.next


def print_list(head):
    current = head
    l = []
    while current is not None:
        l.append(current.val)
        current = current.next
    print(l)


def main():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print_list(head)

    head = reverseBetween(head, 2, 4)
    print_list(head)

    head = ListNode(3, ListNode(5))
    print_list(head)

    head = reverseBetween(head, 1, 2)
    print_list(head)


if __name__ == "__main__":
    main()
