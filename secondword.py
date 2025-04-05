def process_sentence(sentence):
    """
    Processes a sentence to count the words,
    and identify the second and second-to-last words.
    """
    # Split the sentence into words
    words = sentence.split()

    # Count the total number of words
    word_count = len(words)

    # Get the second word and second-to-last word
    if word_count >= 2:  # Ensure there are at least two words
        second_word = words[1]  # Index 1 for the second word
        second_last_word = words[-2]  # Index -2 for the second-to-last word
    else:
        # Handle cases with fewer than two words
        second_word = "Not enough words"
        second_last_word = "Not enough words"

    # Print the results
    print(f"Word Count: {word_count}")
    print(f"Second Word: {second_word}")
    print(f"Second-to-Last Word: {second_last_word}")

# Example usage
sentence = input("Enter a sentence: ")
process_sentence(sentence)