def countRainbow(cls, input1):
    needed = "ROYGBIV"
    freq = {}
    for ch in input1:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in needed:
        if ch not in freq:
            return 0
    min_count = len(input1)
    for ch in needed:
        if freq[ch] < min_count:
            min_count = freq[ch]
    return min_count

# Example Usage:

# input1 : vgyrbvooygibirg
# Output : 2
# Explanation:
# Here, the string S is "vgyrbvooygibirg". We can see that:
# * The colour violet has 2 occurrences.
# * The colour indigo has 2 occurrences.
# * The colour blue has 2 occurrences.
# * The colour green has 3 occurrences.
# * The colour yellow has 2 occurrences.
# * The colour orange has 2 occurrences.
# * The colour red has 2 occurrences,
# The total number of rainbows that can be formed using the given colours is 2. Hence, 2 is returned as the output