import re
from project.api.errors import PayloadException
def check_json(expectedFields, data):
    '''Check request payload, returns missing keys'''
    if not data:
        return 'json'

    for f in expectedFields:
        try:
            data[f]
        except:
            return f

def check_lenght(sentence):
    '''Check if sentence is long enough to encode'''
    if len(sentence) < 4:
        raise PayloadException(
            message='Sentence is too short to be encoded!'
        )
    return sentence

def check_list(sentence, words_list):
    '''Check if list of words and sentence
     contains the same amount of words '''
    words = re.findall(r'\w+', sentence)
    if len(words_list) != len(words):
        raise PayloadException(
            message='List contains less words than sentence!'
        )
    return words_list