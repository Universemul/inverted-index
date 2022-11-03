import unittest

from invertedIndex.core import InvertedIndex
from invertedIndex.tokenize.base import Tokenizer


class UseCaseTest(unittest.TestCase):
    def setUp(self):
        self.tokenizer = Tokenizer()
        self.index = InvertedIndex(self.tokenizer)

    def test_invertedindex_with_tokenizer(self):
        sentence = "Bonjour tout le moNde."
        for token in self.tokenizer.analyze(sentence):
            self.index.add(token, "doc1")
        assert "bonjour" in self.index
        assert "monde" in self.index
        assert "le" not in self.index
