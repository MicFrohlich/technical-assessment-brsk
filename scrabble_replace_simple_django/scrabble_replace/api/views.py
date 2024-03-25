# api/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.replace_words import replace_words
from .utils import load_word_list

@api_view(['POST'])
def replace_words_api(request):
    sentence = request.data.get('sentence', '')
    word_list = load_word_list('./api/words_alpha.txt')
    new_sentence = replace_words(sentence, word_list)
    return Response({'new_sentence': new_sentence})

# Add custom endpoints for custom requests
# /api/generate-sentence/
# This endpoint generates a random sentence of a specified length using words from a word list. The length of the sentence can be controlled by a query parameter. 
# length: Integer (optional) - Specifies the length of the generated sentence.

# /api/matching-words/<word>/
# This endpoint returns a list of words that start with the same letter and have the same length as the input word. This list is generated each time the endpoint is called.
# word: String - The input word for which matching words are to be generated.

# /api/replace-sentence/
# This endpoint takes a sentence as input and replaces each word in the sentence with a randomly chosen word that starts with the same letter and has the same length. If no matching word is found, the original word is returned.

# /api/random-word/
#  This endpoint returns a random word from the word list that starts with a specified letter and has a specified length. If no matching word is found, a random word from the list is returned.
# letter: String (optional) - Specifies the starting letter of the word.
# length: Integer (optional) - Specifies the length of the word.