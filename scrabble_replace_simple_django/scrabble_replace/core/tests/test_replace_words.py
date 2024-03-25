from django.test import TestCase

from api.utils import load_word_list

class TestWordList(TestCase):
    def test_word_list(self):
        word_list = load_word_list('./api/words_alpha.txt')        # Check if words are in alphabetical order
        
        # self.assertEqual(word_list, sorted(word_list), "Error: Words not in alphabetical order")
        # Error: Words not in alphabetical order: 'abacay' before 'abacas'

        # Check if words starting with the same letter are always getting longer
        # prev_word = ''
        # for word in word_list:
        #     if prev_word and word.startswith(prev_word[0]) and len(word) <= len(prev_word):
        #         self.fail(f"Error: Words starting with '{prev_word[0]}' not getting longer: '{prev_word}' > '{word}'")
        #     prev_word = word
        # Error: Words starting with 'a' not getting longer: 'aahing' > 'aahs'

        # Check if no special characters are present
        for word in word_list:
            self.assertTrue(word.isalpha(), f"Error: Special character found: '{word}'")

        # print("All assumptions are valid.") Removed just for neatness but kept as comment

    def test_length_order(self):
        word_list = load_word_list("./api/words_alpha.txt")
        prev_word = ''
        for word in word_list:
            
            if prev_word and word.startswith(prev_word[0]) and len(word) < len(prev_word):
                self.fail(f"Error: Words starting with '{prev_word[0]}' not getting longer: '{prev_word}' > '{word}'")
            prev_word = word