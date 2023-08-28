# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depth_one = 0
    cur = descendantOne
    while cur != topAncestor:
        depth_one +=1
        cur = cur.ancestor

    depth_two = 0
    cur = descendantTwo
    while cur != topAncestor:
        depth_two += 1
        cur = cur.ancestor

    starting_one = descendantOne
    starting_two = descendantTwo
    diff = abs(depth_one - depth_two)
    if depth_one > depth_two:
        while diff > 0:
            starting_one = starting_one.ancestor
            diff -= 1
    else:
        while diff > 0:
            starting_two = starting_two.ancestor
            diff -= 1

    if starting_one == starting_two:
        return starting_one
    while starting_one != starting_two:
        starting_one = starting_one.ancestor
        starting_two = starting_two.ancestor
    return starting_one
        
    


def main():
    A = AncestralTree("A")
    B = AncestralTree("B")
    B.ancestor = A  # type: ignore

    print(A)


if __name__ == "__main__":
    main()
