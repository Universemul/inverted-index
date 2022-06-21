import os
import unittest

from invertedIndex.core import InvertedIndex
from invertedIndex.configuration import JsonConfig


class JsonConfigurationTest(unittest.TestCase):

    def setUp(self):
        # use temporary file
        self.json_index = InvertedIndex(config=JsonConfig(output_file="test.data"))
        self.inmemory_index = InvertedIndex()
        self.data = [
            ('toto', 'document1.txt'),
            ('david', 'document1.txt'),
            ('house', 'document2.txt'),
            ('word', 'document2.txt'),
            ('word', 'document1.txt'),
            ('word', 'document3.txt')
        ]

    def test_json_config(self):
        for item in self.data:
            self.json_index.add(item[0], item[1])
        assert os.path.exists("test.data") is True
        index = InvertedIndex(config=JsonConfig(output_file="test.data"))
        assert len(index.terms()) == 4
        os.remove("test.data")

    def test_add_element_after_loading_existing_documents_json_config(self):
        for item in self.data:
            self.json_index.add(item[0], item[1])
        assert os.path.exists("test.data") is True
        self.json_index.add("haha", "document1.txt")
        assert len(self.json_index.terms()) == 5
        os.remove("test.data")
