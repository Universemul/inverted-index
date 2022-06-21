import typing

from . import Terms
from .exceptions import NotExistingTerm
from .configuration import InMemoryConfig, Config
from .model import Item
from .tokenize import Tokenizer


class InvertedIndex:
    """
    InvertedIndex structure using
    """

    DOCUMENT_DOES_NOT_EXIST = 'The specified document does not exist'
    TERM_DOES_NOT_EXIST = 'The specified term does not exist'

    def __init__(self, tokenizer=None, config: Config = None):
        self._config = config or InMemoryConfig()
        self._terms = self._config.load()
        self._tokenizer = tokenizer or Tokenizer(delimiter=' ')

    def __contains__(self, term: str):
        return term in self._terms

    def __getitem__(self, term: str):
        return self._terms.get(term)

    def tokenize(self, term: str) -> typing.Iterator[str]:
        return self._tokenizer.split(term)

    def add(self, term: str, document: str):
        if term in self._terms:
            self._terms[term].inc(document)
        else:
            self._terms[term] = Item([document])
        self._config.save(self._terms)

    def bulk(self, term, documents: typing.List[str]):
        if term in self._terms:
            self._terms[term].bulk(documents)
        else:
            self._terms[term] = Item(documents)
        self._config.save(self._terms)

    def clear(self):
        """
        Reset the state of the InvertedIndex. Only the configuration remains
        """
        self._terms = Terms()

    def delete_term(self, term: str):
        """
        Delete a term if present otherwise raise an NotExistingTerm exception
        """
        if term not in self._terms:
            raise NotExistingTerm(self.TERM_DOES_NOT_EXIST)
        self._terms.pop(term)

    def delete_document(self, document: str):
        """
        Delete a document in the InvertedIndex. Be careful before launch this method. It can be be long
        """
        for _, item in self._terms.items():
            item.delete_document(document)

    def exact_match(self, term: str):
        """
        Return all documents related to the specified term. It will do an exact match
        """
        if term not in self._terms:
            raise NotExistingTerm(self.TERM_DOES_NOT_EXIST)
        return self._terms[term]

    def terms(self):
        return list(self._terms)