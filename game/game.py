import random
import time

# Dictionary of letter values for Scrabble
LETTER_VALUES = {
    'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
    'D': 2, 'G': 2,
    'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'K': 5,
    'J': 8, 'X': 8,
    'Q': 10, 'Z': 10
}

def load_dictionary():
    """
    Load a dictionary file to check valid words. This is useful for ensuring
    that only real words are accepted in the game.
    
    Returns:
        A set containing all the valid words from the dictionary file.
    """
    try:
        with open('words.txt') as f:
            return set(word.strip().upper() for word in f)
    except FileNotFoundError:
        print("Dictionary file not found.")
        return set()

DICTIONARY = load_dictionary()

def calculate_score(word):
    """
    Calculate the Scrabble score for a given word.

    Args:
        word (str): The word for which to calculate the score.

    Returns:
        int: The total score of the word based on Scrabble letter values.

    Raises:
        ValueError: If the word contains non-alphabetical characters.
    """
    score = 0
    if not word.isalpha():
        raise ValueError("Word contains invalid characters.")
    
    # Convert the word to uppercase and calculate the score
    for letter in word.upper():
        score += LETTER_VALUES.get(letter, 0)
    return score

def generate_word_length():
    """
    Generate a random word length requirement for the game.

    Returns:
        int: A random integer between 3 and 7, representing the required word length.
    """
    return random.randint(3, 7)

def is_valid_word(word):
    """
    Check if the given word is valid by looking it up in the dictionary.

    Args:
        word (str): The word to check for validity.

    Returns:
        bool: True if the word is valid, False otherwise.
    """
    return word.upper() in DICTIONARY

def get_user_word(expected_length):
    """
    Prompt the user to enter a word of a specific length within a 15-second limit.

    Args:
        expected_length (int): The expected length of the word to be entered.

    Returns:
        tuple: A tuple containing the word entered by the user and the time taken.

    Raises:
        ValueError: If the word entered by the user does not match the expected length.
    """
    start_time = time.time()  # Start the timer
    word = input(f"Enter a word of {expected_length} letters (15-second limit): ")
    end_time = time.time()  # End the timer
    
    time_taken = end_time - start_time  # Calculate the time taken
    
    if time_taken > 15:
        raise ValueError("Time limit exceeded. Please be faster next time!")
    
    # Check if the word length matches the expected length
    if len(word) != expected_length:
        raise ValueError(f"Word must be exactly {expected_length} letters long.")
    
    return word, time_taken

def adjust_score_based_on_time(score, time_taken):
    """
    Adjust the score based on the time taken by the user. The faster the input,
    the higher the score.

    Args:
        score (int): The original score based on the word.
        time_taken (float): The time taken by the user to enter the word.

    Returns:
        int: The adjusted score based on the time taken.
    """
    if time_taken <= 0:
        time_taken = 1  # Avoid division by zero
    # Scale the score: faster input yields higher score
    time_bonus = max(1, (15 - time_taken) / 15)  # Bonus factor between 1 and 0 (inclusive)
    return int(score * time_bonus)

def play_game():
    """
    Main function to play the Scrabble score game. This function handles the game loop,
    scoring, and user input.
    """
    total_score = 0
    round_count = 0
    used_words = set()  # Set to keep track of words that have already been entered
    
    # Continue the game for 10 rounds
    while round_count < 10:
        expected_length = generate_word_length()
        try:
            word, time_taken = get_user_word(expected_length)
            
            if word.upper() in used_words:
                print("You've already used that word. Try another one.")
                continue
            
            if not is_valid_word(word):
                print("Invalid word. Try again.")
                continue

            # Add the word to the set of used words
            used_words.add(word.upper())
            
            # Calculate the initial score
            score = calculate_score(word)
            # Adjust the score based on the time taken
            adjusted_score = adjust_score_based_on_time(score, time_taken)
            total_score += adjusted_score
            round_count += 1
            print(f"Round {round_count} Score: {adjusted_score}, Total Score: {total_score}")
        except ValueError as e:
            print(e)
            continue

    print(f"Game Over! Your total score is {total_score}")

if __name__ == "__main__":
    play_game()
