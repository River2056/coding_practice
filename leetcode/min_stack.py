from common.models import Node

class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(Node(val, val))
        else:
            last = self.stack[len(self.stack) - 1]
            min_val = min(last.min, val)
            self.stack.append(Node(val, min_val))

    def pop(self) -> None:
        node = self.stack.pop()
        return node.val

    def top(self) -> int:
        return self.stack[len(self.stack) - 1].val

    def getMin(self) -> int:
        return self.stack[len(self.stack) - 1].min

    def __str__(self):
        s = []
        for node in self.stack:
            s.append(str(node))
        return ", ".join(s)


def main():
    input = [
        "MinStack",
        "push",
        "push",
        "push",
        "top",
        "pop",
        "getMin",
        "pop",
        "getMin",
        "pop",
        "push",
        "top",
        "getMin",
        "push",
        "top",
        "getMin",
        "pop",
        "getMin",
    ]
    input_val = [
        [],
        [2147483646],
        [2147483646],
        [2147483647],
        [],
        [],
        [],
        [],
        [],
        [],
        [2147483647],
        [],
        [],
        [-2147483648],
        [],
        [],
        [],
        [],
    ]
    stack = None
    for k, s in enumerate(input):
        if s == "MinStack":
            stack = MinStack()
        elif s == "push":
            print("push")
            stack.push(input_val[k][0])  # type: ignore
        elif s == "top":
            print("top")
            stack.top()  # type: ignore
        elif s == "pop":
            print("pop")
            stack.pop()  # type: ignore
        else:
            print("getMin")
            stack.getMin()  # type: ignore
        print(stack)


if __name__ == "__main__":
    main()
