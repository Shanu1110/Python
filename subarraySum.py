def subarraySum(nums, k):
    count = 0
    curr_sum = 0
    sum_map = {0: 1}

    for num in nums:
        curr_sum += num
        if (curr_sum - k) in sum_map:
            count += sum_map[curr_sum - k]
        sum_map[curr_sum] = sum_map.get(curr_sum, 0) + 1

    return count