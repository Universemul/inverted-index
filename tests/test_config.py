import os
import unittest

from invertedIndex.core import InvertedIndex
from invertedIndex.configuration import JsonConfig


class JsonConfigurationTest(unittest.TestCase):

    def setUp(self):
        self.filename = "test2.data"
        fo = open(self.filename, 'w')
        fo.close()
        self.json_index = InvertedIndex(config=JsonConfig(output_file=self.filename))
        self.inmemory_index = InvertedIndex()
        self.data = [
            ('toto', 'document1.txt'),
            ('david', 'document1.txt'),
            ('house', 'document2.txt'),
            ('word', 'document2.txt'),
            ('word', 'document1.txt'),
            ('word', 'document3.txt')
        ]

    def tearDown(self) -> None:
        os.remove(self.filename)

    def test_json_config(self):
        for item in self.data:
            self.json_index.add(item[0], item[1])
        index = InvertedIndex(config=JsonConfig(output_file=self.filename))
        assert len(index.terms()) == 4

    def test_add_element_after_loading_existing_documents_json_config(self):
        for item in self.data:
            self.json_index.add(item[0], item[1])
        self.json_index.add("haha", "document1.txt")
        assert len(self.json_index.terms()) == 5