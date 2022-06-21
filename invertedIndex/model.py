import json
from typing import List

from invertedIndex.encoder import DefaultEncoder


class Item:

    def __init__(self, documents: List[str]):
        self.frequency = 1
        self.documents = set(documents)

    def inc(self, document: str):
        self.frequency += 1
        self.documents.add(document)

    def bulk(self, documents: List[str]):
        self.frequency += len(documents)
        self.documents |= set(documents)

    def delete_document(self, document: str):
        if document in self.documents:
            self.frequency -= 1
            self.documents.remove(document)

    def __repr__(self):
        return f"<Item: Found {self.frequency} times in {','.join(self.documents)} documents>"

    def __eq__(self, other):
        return self.frequency == other.frequency and self.documents == other.documents

    def __iter__(self):
        yield from {
            "frequency": self.frequency,
            "documents": self.documents
        }.items()

    def __str__(self):
        return json.dumps(dict(self), cls=DefaultEncoder, ensure_ascii=False)

    def to_json(self):
        return self.__str__()
