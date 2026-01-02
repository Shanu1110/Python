def maxPathSum(root):
    max_sum = float('-inf')

    def max_gain(node):
        nonlocal max_sum
        if node is None:
            return 0
        
        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)
        
        current_path_sum = node.val + left_gain + right_gain
        
        max_sum = max(max_sum, current_path_sum)
        
        return node.val + max(left_gain, right_gain)

    max_gain(root)
    return max_sum