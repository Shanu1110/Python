def diameterOfBinaryTree(root):
    diameter = 0

    def height(node):
        nonlocal diameter
        if node is None:
            return 0
        
        left_height = height(node.left)
        right_height = height(node.right)
        
        diameter = max(diameter, left_height + right_height)
        
        return max(left_height, right_height) + 1

    height(root)
    return diameter