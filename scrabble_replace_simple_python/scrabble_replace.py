import random
from utils import load_word_list
# from tests.test_word_list import test_word_list

#    below is script that replaces all the words in a sentence with a valid same first letter, same length word if same length word possible
def replace_words(sentence, word_list):
    words = sentence.split()
    new_sentence = []
    if len(word_list) > 0:
        for word in words:
            same_first_letter_words = [w for w in word_list if w.lower().startswith(word.lower()[0]) and len(w) == len(word) and w.lower() != word.lower()]
            if same_first_letter_words:
                new_sentence.append(random.choice(same_first_letter_words))
            else:
                new_sentence.append(word)
        return ' '.join(new_sentence)
    else:
        return "Something went wrong"

#  TODO add main below to test via cli
if __name__ == '__main__':
    word_list = load_word_list('words_alpha.txt')
    # Run tests before replacing words
    # if test_word_list(word_list):
    sentence = input('Enter a sentence: ')
    new_sentence = replace_words(sentence, word_list)
    print('New Sentence:', new_sentence)
    # else:
    #     print("Test Failed")