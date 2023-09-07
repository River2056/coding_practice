from common.models import ListNode


def print_list(head):
    res = []
    cur = head
    while cur is not None:
        res.append(cur.val)
        cur = cur.next
    print(res)


def convert_from_list_to_listnode(array):
    nodes = [ListNode(e) for e in array]
    i = 1
    for node in nodes:
        next_node = nodes[i] if i < len(nodes) else None
        node.next = next_node
        i += 1
    return nodes[0]
