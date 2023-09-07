from common.models import TreeNode

class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def dfs(node, p, q):
            if node is None:
                return 0
            left = dfs(node.left, p, q)
            right = dfs(node.right, p, q)
            cur = node.val == p.val or node.val == q.val
            if left + right + cur >= 2 and self.ans is None:
                self.ans = node
            return left + right + cur

        dfs(root, p, q)
        return self.ans  # type: ignore
