import re
import random
from difflib import SequenceMatcher


class WeirdText(object):
    '''Service that provides encoding/decoding
    functionality'''
    def encode_word(self, letters, seed):
        '''Shuffle letters based on seed,
        returns shuffled letters.'''
        random.seed(seed)
        order = list(range(len(letters)))
        random.shuffle(order)
        random.shuffle(list(range(len(letters))))
        return ''.join([letters[i] for i in order])

    def decode_word(self, letters, order):
        '''Decodes word based on order list generated
        from seed.'''
        decoded_zip = sorted(zip(letters, order), key=lambda k: k[1])
        return ''.join(list(zip(*decoded_zip))[0])

    def order_generator(self, letters, seed):
        '''Generates order in order to decode word'''
        random.seed(seed)
        order = list(range(len(letters)))
        random.shuffle(order)
        return order

    def hash_generator(self, letters):
        '''Generates seed for encoding/decoding
        based on alphabetical ordereded letters in word'''
        return hash(''.join(sorted(letters)))

    def encode_sentence(self, sentence):
        '''Perform encoding operation on every
        word that contains more than 3 letters.'''
        words_to_encode = re.findall(r'\w+', sentence)
        encoded_words = []
        for w in words_to_encode:
            if len(w) > 3:
                seed = self.hash_generator(w)
                encoded = self.encode_word(w[1:-1], seed)
                encoded_words.append(w.replace(w[1:-1], encoded))
            else:
                encoded_words.append(w)
        for word, weird_word in zip(words_to_encode, encoded_words):
            sentence = sentence.replace(word, weird_word, 1)
        return sentence

    def decode_sentence(self, sentence):
        '''Reverts encoding algorithm. Works only with
        sentences encoded by this alghoritm'''
        words_to_decode = re.findall(r'\w+', sentence)
        decoded_words = []
        for w in words_to_decode:
            if len(w) > 3:
                seed = self.hash_generator(w)
                order = self.order_generator(w[1:-1], seed)
                decoded = self.decode_word(w[1:-1], order)
                decoded_words.append(w.replace(w[1:-1], decoded))
            else:
                decoded_words.append(w)
        for word, decoded_word in zip(words_to_decode, decoded_words):
            sentence = sentence.replace(word, decoded_word, 1)
        return sentence

    def decode_based_on_list(self, sentence, orginal_words):
        '''Uses difflib to estimate similarity between encoded
        and decoded words. Tries to decode sentence based on 
        provided list of orginal words.'''
        words_to_decode = re.findall(r'\w+', sentence)
        for encoded in words_to_decode:
            prob_list = [(index,
                          SequenceMatcher(
                              None, encoded[1:-1], orginal[1:-1]).ratio(),
                          orginal) for index, orginal in enumerate(orginal_words)]
            decoded = max(prob_list, key=lambda x: x[1])[2]
            sentence = sentence.replace(encoded, decoded, 1)
        return sentence
