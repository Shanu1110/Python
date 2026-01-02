def firstRepeat(lst):
    seen = set()
    result = -1
    for i in range(len(lst)-1, -1, -1):
        if lst[i] in seen:
            result = lst[i]
        else:
            seen.add(lst[i])
    return result