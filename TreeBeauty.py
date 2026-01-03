# Python 3
import sys
sys.setrecursionlimit(1 << 25)
MOD = 10**9 + 7

def build_spf(m):
    spf = list(range(m+1))
    for i in range(2, int(m**0.5) + 1):
        if spf[i] == i:
            for j in range(i*i, m+1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf

def square_free_kernel(x, spf):
    if x == 0:
        return None  # special zero
    k = 1
    while x > 1:
        p = spf[x] if spf[x] != x else x
        cnt = 0
        while x % p == 0:
            x //= p
            cnt ^= 1  # parity
        if cnt == 1:
            k *= p
    return k

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
g = [[] for _ in range(n)]
for _ in range(n-1):
    u,v = map(int, sys.stdin.readline().split())
    u -= 1; v -= 1
    g[u].append(v); g[v].append(u)

maxA = max(a)
spf = build_spf(maxA if maxA > 1 else 2)
kernels = [square_free_kernel(x, spf) for x in a]

ans = 0

def dfs(u, p):
    # returns: map kernel->count, size, zero_count, beauty_u
    mp = {}
    size = 1
    zeros = 1 if kernels[u] is None else 0
    if kernels[u] is not None:
        mp[kernels[u]] = 1
    beauty_u = 0
    for v in g[u]:
        if v == p: continue
        child_mp, child_size, child_zeros, child_beauty = dfs(v, u)
        beauty_u = (beauty_u + child_beauty) % MOD
        # small-to-large
        if len(child_mp) > len(mp):
            mp, child_mp = child_mp, mp
        # merge counts
        for k, c in child_mp.items():
            prev = mp.get(k, 0)
            mp[k] = prev + c
        size += child_size
        zeros += child_zeros
    # compute beauty at u
    # positive-only case (no zeros): sum C(cnt, 2)
    if zeros == 0:
        for c in mp.values():
            beauty_u = (beauty_u + (c * (c - 1) // 2)) % MOD
    else:
        # zeros pair with everything
        beauty_u = (beauty_u + zeros * (size - zeros) + (zeros * (zeros - 1) // 2)) % MOD
        # plus pairs among equal kernels (nonzero)
        for c in mp.values():
            beauty_u = (beauty_u + (c * (c - 1) // 2)) % MOD
    return mp, size, zeros, beauty_u

_, _, _, total = dfs(0, -1)
print(total % MOD)
