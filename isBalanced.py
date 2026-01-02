def isBalanced(root):
    def check_balance(node):
        if node is None:
            return 0
        
        left_height = check_balance(node.left)
        if left_height == -1:
            return -1
        
        right_height = check_balance(node.right)
        if right_height == -1:
            return -1
        
        if abs(left_height - right_height) > 1:
            return -1
        
        return max(left_height, right_height) + 1
    
    return check_balance(root) != -1