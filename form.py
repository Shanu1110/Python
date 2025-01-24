def max_removed_worth(binary_string, worth):
    n = len(binary_string)
    total_worth = sum(worth)  # Total worth of the original string
    keep_worth = worth[0]  # Initialize with the worth of the first character
    
    # Traverse the string to build the longest alternating sequence
    for i in range(1, n):
        # If the current character continues the alternating pattern, keep it
        if binary_string[i] != binary_string[i - 1]:
            keep_worth += worth[i]
        else:
            # Remove the character with the lower worth
            keep_worth += max(worth[i], worth[i - 1])
            worth[i] = max(worth[i], worth[i - 1])  # Update worth to track the maximum
    
    # Calculate the worth of removed characters
    removed_worth = total_worth - keep_worth
    return removed_worth

# Example usage:
binary_string = input()
worth = list(map(int, input().split()))
print(max_removed_worth(binary_string, worth))