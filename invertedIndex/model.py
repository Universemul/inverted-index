from typing import List


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
