class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{ {self.val if self is not None else None},{self.next if self.next is not None else None} }"


class Node:
    def __init__(self, val: int, min: int):
        self.val = val
        self.min = min

    def __str__(self):
        return f"{{ val: {self.val}, min: {self.min} }}"


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
