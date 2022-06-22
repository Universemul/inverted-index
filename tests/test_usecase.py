import unittest


from invertedIndex.core import InvertedIndex
from invertedIndex.tokenize import Tokenizer


class UseCaseTest(unittest.TestCase):

    def setUp(self):
        self.tokenizer = Tokenizer()
        self.index = InvertedIndex(self.tokenizer)

    def test_invertedindex_with_tokenizer(self):
        sentence = "There is no one who loves pain itself, who seeks after it and wants to have it, simply because it is pain..."
        for token in self.tokenizer.split(sentence):
            self.index.add(token, "doc1")
        assert 'loves' in self.index
        assert 'pain itself' not in self.index


