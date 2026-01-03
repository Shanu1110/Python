import sys
import math

def good_exists(arr, p):
    n = len(arr)
    g = 0
    for x in arr:
        g = math.gcd(g, x)
    if g == p:
        # whole array gcd = p
        if n > 1:
            return True
        else:
            return False
    elif g % p == 0:
        # check reduced gcd
        reduced_g = 0
        for x in arr:
            reduced_g = math.gcd(reduced_g, x // p)
        return reduced_g == 1
    else:
        return False

def main():
    input_data = sys.stdin.read().split()
    it = iter(input_data)
    n, p, q = int(next(it)), int(next(it)), int(next(it))
    arr = [int(next(it)) for _ in range(n)]
    yes_count = 0
    for _ in range(q):
        i, j = int(next(it)), int(next(it))
        arr[i-1] = j
        if good_exists(arr, p):
            yes_count += 1
    print(yes_count)
    
if __name__ == "__main__":
    main()