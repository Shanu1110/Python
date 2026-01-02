def isValidBST(root):
    def dfs(node, low, high):
        if node is None:
            return True
        if not (low < node.val < high):
            return False
        return (dfs(node.left, low, node.val) and
                dfs(node.right, node.val, high))