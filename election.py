def majorityElement(a, n):
    vote_count = 0
    candidate = 0
    for i in range(n):
        if vote_count == 0:
            candidate = a[i]
        # Election counting:
        if a[i] == candidate:
            vote_count += 1
        else:
            vote_count -= 1
    return candidate