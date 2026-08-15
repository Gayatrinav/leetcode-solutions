class Solution:
    def longestZigZag(self, root):
        self.answer = 0

        def dfs(node, left, right):
            if node is None:
                return

            self.answer = max(self.answer, left, right)

            # Move left → next must move right
            dfs(node.left, 0, left + 1)

            # Move right → next must move left
            dfs(node.right, right + 1, 0)

        dfs(root, 0, 0)

        return self.answer