class Solution:
    def goodNodes(self, root):
        def dfs(node, max_val):
            if node is None:
                return 0

            count = 0

            if node.val >= max_val:
                count = 1
                max_val = node.val

            count += dfs(node.left, max_val)
            count += dfs(node.right, max_val)

            return count

        return dfs(root, root.val)