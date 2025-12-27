def maxSubArray(a, n):
    max_sum = a[0]
    current_sum = a[0]
    for i in range(1, n):
        current_sum = max(current_sum + a[i], a[i])
        max_sum = max(max_sum, current_sum)
    return max_sum

if __name__ == "__main__":
    a = list(map(int, input().split()))
    n = len(a)
    print(maxSubArray(a, n))