import unittest

import pytest

from invertedIndex.core import InvertedIndex
from invertedIndex.exceptions import NotExistingTerm


class InvertedIndexTest(unittest.TestCase):

    def setUp(self):
        self.index = InvertedIndex()
        self.index.add('toto', 'document1.txt')
        self.index.add('david', 'document1.txt')
        self.index.add('house', 'document2.txt')
        self.index.add('word', 'document2.txt')
        self.index.add('word', 'document1.txt')
        self.index.add('word', 'document3.txt')

    def test_contains(self):
        assert 'word' in self.index
        assert 'house' in self.index
        assert 'david' in self.index

        assert 'HouSe' not in self.index
        assert 'titi' not in self.index

    def test_get_item(self):
        assert self.index['word'].documents == {'document1.txt', 'document2.txt', 'document3.txt'}
        assert self.index['toto'].documents == {'document1.txt'}

    def test_delete_term(self):
        self.index.delete_term('word')
        assert 'words' not in self.index

        with pytest.raises(NotExistingTerm):
            self.index.delete_term('titi')

    def test_exact_match(self):
        match = self.index.exact_match('word')
        assert match.frequency == 3
        assert match.documents == {'document1.txt', 'document2.txt', 'document3.txt'}
        with pytest.raises(NotExistingTerm):
            self.index.exact_match('titi')

    def test_clear(self):
        self.index.clear()
        assert self.index.terms() == []
