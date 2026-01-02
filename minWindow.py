def minWindow(s, t):
    need = counter(t)
    missing = len(t)
    l = start = end = 0
    for r, char in enumerate(s, 1):
        if need[char] > 0:
            missing -= 1
        need[char] -= 1

        while missing == 0:
            if end == 0 or r - l < end - start:
                start, end = l, r
            need[s[l]] += 1
            if need[s[l]] > 0:
                missing += 1
            l += 1
    return s[start:end] 