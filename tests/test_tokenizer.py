import unittest

from invertedIndex.tokenizer import Tokenizer


class TokenizerTest(unittest.TestCase):

    def setUp(self):
        self.tokenizer = Tokenizer()
        self.tokenizer_with_pipe_delimiter = Tokenizer('|')

    def test_default_tokenizer(self):
        assert list(self.tokenizer.split('Hello world')) == ['Hello', 'world']

    def test_tokenizer_with_pipe(self):
        assert list(self.tokenizer_with_pipe_delimiter.split('Hello world')) == ['Hello world']
        assert list(self.tokenizer_with_pipe_delimiter.split('Hello|world')) == ['Hello', 'world']
