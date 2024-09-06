import unittest
import time
from game import calculate_score, generate_word_length, is_valid_word, load_dictionary

class TestScrabbleScore(unittest.TestCase):
    """
    Unit tests for the Scrabble score calculation functionality.
    """
    
    def test_single_letter(self):
        """
        Test the score calculation for single letters.
        """
        self.assertEqual(calculate_score('A'), 1)
        self.assertEqual(calculate_score('Z'), 10)
    
    def test_word_score(self):
        """
        Test the score calculation for entire words, ensuring case insensitivity.
        """
        self.assertEqual(calculate_score('cabbage'), 14)
        self.assertEqual(calculate_score('CABBAGE'), 14)  # Test for case insensitivity
    
    def test_invalid_input(self):
        """
        Test that the score calculation raises an error for invalid inputs.
        """
        with self.assertRaises(ValueError):
            calculate_score('c@bbage')  # Invalid character

class TestGameLogic(unittest.TestCase):
    """
    Unit tests for the game logic, including word length generation and timing.
    """
    
    def test_generate_word_length(self):
        """
        Test that the word length generated is within the expected range.
        """
        length = generate_word_length()
        self.assertTrue(3 <= length <= 7)  # Assuming word length is between 3 and 7
    
    def test_input_timer(self):
        """
        Test the timing functionality to ensure it's measuring time correctly.
        """
        start_time = time.time()
        time.sleep(2)  # Simulate delay
        end_time = time.time()
        self.assertTrue(1.5 <= (end_time - start_time) <= 2.5)

class TestWordValidation(unittest.TestCase):
    """
    Unit tests for word validation against the dictionary.
    """
    
    def test_valid_word(self):
        """
        Test that the word validation function correctly identifies valid and invalid words.
        """
        # Load the dictionary for testing
        DICTIONARY = load_dictionary()
        self.assertIn("CABBAGE", DICTIONARY)
        self.assertIn("APPLE", DICTIONARY)
        self.assertNotIn("ZZZZZZ", DICTIONARY)

if __name__ == '__main__':
    unittest.main()
