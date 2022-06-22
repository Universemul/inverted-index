import json
import os
import typing

from invertedIndex import Terms
from invertedIndex.encoder import DefaultEncoder


class Config:

    def save(self, documents: Terms):
        raise NotImplemented

    def load(self) -> Terms:
        raise NotImplemented


class InMemoryConfig(Config):

    def save(self, documents: Terms):
        pass

    def load(self) -> Terms:
        return Terms()


class JsonConfig(Config):

    def __init__(self, output_file: str = "inverted_index_data"):
        self._output_file = output_file

    def save(self, documents: Terms):
        print(documents)
        with open(self._output_file, 'w') as _f:
            _f.write(json.dumps(documents, cls=DefaultEncoder))

    def load(self) -> Terms:
        if os.path.exists(self._output_file):
            with open(self._output_file, 'r') as _f:
                try:
                    return json.loads(_f.read())
                except json.JSONDecodeError as e:
                    return Terms()
        return Terms()

