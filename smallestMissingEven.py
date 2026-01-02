def smallest_missing_even(cls, input1, input2):
    even_numbers = set()
    for num in input1:
        if num % 2 == 0:
            even_numbers.add(num)
            if num > max_even:
                max_even = num
    if not even_numbers:
        return 2
    for i in range(2, max_even + 1, 2):
        if i not in even_numbers:
            return i
    return max_even + 2