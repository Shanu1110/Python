def longestUniqueSubstring(s):
    mp = {}
    l = ans = 0
    for r, ch in enumerate(s):
        if ch in mp and mp[ch] >= l:
            l = mp[ch] + 1
        mp[ch] = r
        ans = max(ans, r - l + 1)
    return ans