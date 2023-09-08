from common.models import ListNode
from common.functions import print_list
from common.functions import convert_from_list_to_listnode


def splitListToParts(head: ListNode, k: int) -> list[ListNode]:
    res = []
    length = 0
    cur = head
    while cur is not None:
        length += 1
        cur = cur.next

    if length < k:
        cur = head
        while cur is not None:
            next_node = cur.next
            cur.next = None
            res.append(cur)
            cur = next_node
            k -= 1
        for _ in range(k):
            res.append(None)
    else:
        cur = head
        group_count = length // k
        left_overs = length % k
        for _ in range(k):
            counter = 1
            dest = group_count
            if left_overs > 0:
                dest += 1
                left_overs -= 1
            group_head = cur
            while counter != dest:
                counter += 1
                cur = cur.next  # type: ignore
            next_node = cur.next  # type: ignore
            cur.next = None  # type: ignore
            cur = next_node
            res.append(group_head)
    return res


def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    head = convert_from_list_to_listnode(arr)
    arr = splitListToParts(head, 3)
    for node in arr:
        print_list(node)

    arr2 = [1, 2, 3]
    head = convert_from_list_to_listnode(arr2)
    arr2 = splitListToParts(head, 5)
    for node in arr2:
        print_list(node)


if __name__ == "__main__":
    main()
