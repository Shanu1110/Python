def longest_good_subsequence(A, M):
    n = len(A)
    # dp[i] = dictionary {xor_val: length} for subsequences ending at index i
    dp = [dict() for _ in range(n)]
    ans = 0
    
    for i in range(n):
        # Start new subsequence with A[i]
        dp[i][A[i]] = max(dp[i].get(A[i], 0), 1)
        
        # Try to extend from previous indices j < i with A[j] <= A[i]
        for j in range(i):
            if A[j] <= A[i]:
                for xor_val, length in dp[j].items():
                    new_xor = xor_val ^ A[i]
                    dp[i][new_xor] = max(dp[i].get(new_xor, 0), length + 1)
        
        # Check all XOR values at i
        for xor_val, length in dp[i].items():
            if xor_val >= M:
                ans = max(ans, length)
    
    return ans


# Example usage:
if __name__ == "__main__":
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    print(longest_good_subsequence(A, M))
