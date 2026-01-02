def countVowels_collected(cls, input1, input2):
    energy = input2
    vowel_count = 0
    forward_vowel_count = 5
    vowels = set('aeiou')
    
    for char in input1:
        if char in vowels:
            if energy >= forward_vowel_count:
                energy += forward_vowel_count
                vowel_count += 1
                forward_vowel_count += 5
        else:
            energy -= 1
    return vowel_count



# def # Example Usage: countVowels_collected(cls, input1, input2):
#     energy = input2
#     vowel_count = 0
#     forward_vowel_count = 5
#     vowels = set('aeiou')
#     for char in input1:
#         if char in vowels:
#             if energy >= forward_vowel_count:
#                 energy += forward_vowel_count
#                 vowel_count += 1
#                 forward_vowel_count += 5
#         else:
#             energy -= 1
#     return vowel_count


# Explanation:
# rallcom
# ukr 44150c
# nail.com
# Here, 5 = bbbbaciou, and the initial energy Lis 4. We can find the total parcels as
# below.
# • Collected 'b' (consonant) -> energy becomes 5
# • Collected 'b' (consonant) -> energy becomes 6
# • Collected 'b' (consonant) -> energy becomes 7
# • Collected 'b' (consonant) -> energy becomes 8
# • Encountered 'a' (first vowel, needs 5) -> has enough energy -> collect it => energy becomes 13 and next vowel cost becomes 10.
# • Encountered 'e' (second vowel, needs 10) -> has enough energy -› collect it -> energy becomes 23 and next vowel cost becomes 15.
# • Encountered I (third vowel, needs 15) -> has enough energy -> collect it -> energy becomes 38 and next vowel cost becomes 20.
# • Encountered o (fourth vowel, needs 20) -> has enough energy →› collect it -> energy becomes 58 and next vowel cost becomes 25.
# • Encountered u (fifth vowel, needs 25) -> has enough energy =› collect it *> energy becomes 83
# Total vowels collected is 5. Hence. 5 is retu
# as the outaut