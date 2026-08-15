class Solution:
    def leafSimilar(self, root1, root2):
        def get_leaves(root):
            if root is None:
                return []

            if root.left is None and root.right is None:
                return [root.val]

            return get_leaves(root.left) + get_leaves(root.right)

        return get_leaves(root1) == get_leaves(root2)