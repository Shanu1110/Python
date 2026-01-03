import sys
sys.setrecursionlimit(1 << 25)

def build_kmp(pattern):
    """KMP automaton: returns pi (prefix function), go table for states 0..m, and terminal array."""
    m = len(pattern)
    # prefix function
    pi = [0] * m
    for i in range(1, m):
        j = pi[i - 1]
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        pi[i] = j
    # go[state][bit] for bit in {0,1}, states 0..m
    go = [[0, 0] for _ in range(m + 1)]
    for s in range(m + 1):
        for bit in (0, 1):
            if s < m and pattern[s] == bit:
                go[s][bit] = s + 1
            else:
                if s == 0:
                    go[s][bit] = 0
                else:
                    go[s][bit] = go[pi[s - 1]][bit]
    terminal = [False] * (m + 1)
    terminal[m] = True
    return go, terminal

def better(a, b):
    """Lexicographic optimization: maximize natural paths, then minimize flips."""
    if a[0] != b[0]:
        return a[0] > b[0]
    return a[1] < b[1]

def add(a, b):
    """Add pair (natural_paths, flips)."""
    return (a[0] + b[0], a[1] + b[1])

def solve_query(N, parent, children, val, M, qbits):
    go, terminal = build_kmp(qbits)
    m = len(qbits)

    # DFS returning a function of incoming automaton state and hit flag:
    # For each node u, we compute two base modes over states:
    # res0[s_in, hit_in]: u not toggled; children cannot flip
    # res1_base[s_in, hit_in]: u toggled; children cannot flip
    # and per child deltas if that child edge is the unique flip causing u toggled.
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def dp_u_base(u, s_in, hit_in, toggled):
        """Compute base contribution for node u when its bit is toggled==False/True,
        and NO child edge flips (u is unmatched if toggled==False, matched if toggled==True).
        Returns (natural_paths, flips) best in subtree."""
        bit_u = val[u] ^ (1 if toggled else 0)
        s_u = go[s_in][bit_u]
        hit_u = hit_in or terminal[s_u]

        # Leaf
        if len(children[u]) == 0:
            return (1 if hit_u else 0, 0)

        # Aggregate children: since we prohibit child edge flips, every child runs in its own base mode with toggled=False
        total_nat = 0
        total_flips = 0
        for v in children[u]:
            # child v is NOT flipped at edge (u, v), so v's bit is not toggled by that edge
            # parent matched status at v is irrelevant here because we disallow flips at v anyway in base
            # Incoming state to child is after reading v's bit (not toggled)
            bit_v = val[v]
            s_v = go[s_u][bit_v]
            hit_v = hit_u or terminal[s_v]
            res_v = dp_u_base(v, s_u, hit_u, toggled=False)
            total_nat += res_v[0]
            total_flips += res_v[1]
        return (total_nat, total_flips)

    @lru_cache(maxsize=None)
    def dp_child_flip(u, s_in, hit_in, child):
        """Compute contribution when u is toggled (by some incident edge),
        and specifically we flip edge (u, child), toggling child's bit.
        Other child edges are not flipped.
        Returns (natural_paths, flips_in_subtrees + 1_for_edge_u_child)."""
        # u toggled
        bit_u = val[u] ^ 1
        s_u = go[s_in][bit_u]
        hit_u = hit_in or terminal[s_u]

        total_nat = 0
        total_flips = 0

        for v in children[u]:
            if v == child:
                # child edge flipped: child's bit toggled
                bit_v = val[v] ^ 1
                s_v = go[s_u][bit_v]
                hit_v = hit_u or terminal[s_v]
                # Inside child's subtree, child is matched; no further incident flips at v
                res_v = dp_u_base(v, s_u, hit_u, toggled=True)
                total_nat += res_v[0]
                total_flips += res_v[1]
                # add cost for flipping (u, v)
                total_flips += 1
            else:
                # other children: no flip, u is matched so they cannot flip (but we already disallow flips in base)
                res_v = dp_u_base(v, s_u, hit_u, toggled=True)
                total_nat += res_v[0]
                total_flips += res_v[1]
        return (total_nat, total_flips)

    # At each node, parent decides among:
    # - u not toggled (mode0): dp_u_base(u, s_in, hit_in, toggled=False)
    # - u toggled via parent (mode1p): dp_u_base(u, s_in, hit_in, toggled=True) + cost 1 for edge (parent,u) if u != root
    # - u toggled via a specific child (mode1c): dp_child_flip(u, s_in, hit_in, child)

    @lru_cache(maxsize=None)
    def dp(u, s_in, hit_in, has_parent):
        """Returns best (natural_paths, flips) for subtree at u, choosing flips at u consistently.
        has_parent indicates if edge (parent, u) exists (False at root).
        """
        # Option A: u not toggled; no child flips possible
        optA = dp_u_base(u, s_in, hit_in, toggled=False)

        # Option B: u toggled via parent (if has_parent)
        optB = None
        if has_parent:
            base1 = dp_u_base(u, s_in, hit_in, toggled=True)
            # add cost of flipping (parent,u)
            optB = (base1[0], base1[1] + 1)

        # Option C: u toggled via one child (try all children)
        optC = None
        for v in children[u]:
            cand = dp_child_flip(u, s_in, hit_in, v)
            if optC is None or better(cand, optC):
                optC = cand

        # Choose best among available options
        best_opt = optA
        if optB is not None and better(optB, best_opt):
            best_opt = optB
        if optC is not None and better(optC, best_opt):
            best_opt = optC
        return best_opt

    # Run from root with initial KMP state 0 and hit=False
    nat_paths, flips = dp(0, 0, False, has_parent=False)
    # We need to maximize natural paths first; cost is M * flips achieving that max
    # dp already did lexicographic optimization. Return cost M * flips and also the count if needed.
    return nat_paths, flips * M

def main():
    input_data = sys.stdin.read().strip().split()
    it = iter(input_data)

    N = int(next(it))
    # Parent array: Parent[0] = 0; for i>0, Parent[i] is parent of i
    parent = [int(next(it)) for _ in range(N)]
    val = [int(next(it)) for _ in range(N)]
    M = int(next(it))
    Q = int(next(it))
    queries = [next(it).strip() for _ in range(Q)]

    # Build children list
    children = [[] for _ in range(N)]
    for i in range(1, N):
        p = parent[i]
        children[p].append(i)

    total_cost = 0
    # Preconvert query strings to bits
    for q in queries:
        qbits = [1 if ch == '1' else 0 for ch in q]
        nat, cost = solve_query(N, parent, children, val, M, qbits)
        total_cost += cost
    print(total_cost)

if __name__ == "__main__":
    main()
