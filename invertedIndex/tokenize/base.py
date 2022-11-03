import abc
import os
import string
from typing import Callable, Iterator, Set

from unidecode import unidecode

_current_dir = os.path.dirname(__file__)


class Tokenizer(metaclass=abc.ABCMeta):
    def __init__(self, delimiter=" "):
        self.delimiter = delimiter
        self._stopwords = self._load_stopwords()

    @abc.abstractmethod
    def get_stopword_file_path(self) -> str:
        pass

    def _load_stopwords(self) -> Set[str]:
        _file_path = os.path.join(
            _current_dir, "../stopwords/", self.get_stopword_file_path()
        )
        if not os.path.exists(_file_path):
            raise FileNotFoundError
        with open(_file_path, "r") as f:
            return set(f.read().splitlines())

    def analyze(self, term: str) -> Iterator[str]:
        tokens = self.tokenize(term)
        apply_func: Callable[[Iterator[str]], Iterator[str]]
        for apply_func in (
            self.lowercase,
            self.text_only,
            self.normalize,
            self.stopwords,
            self.remove_punctuation,
        ):
            tokens = apply_func(tokens)
        yield from tokens

    def tokenize(self, term: str) -> Iterator[str]:
        for token in term.split(self.delimiter):
            yield token

    def remove_punctuation(self, tokens: Iterator[str]) -> Iterator[str]:
        for token in tokens:
            yield token.translate(str.maketrans("", "", string.punctuation))

    def normalize(self, tokens: Iterator[str]) -> Iterator[str]:
        for token in tokens:
            yield unidecode(token)

    def text_only(self, tokens: Iterator[str]) -> Iterator[str]:
        for token in tokens:
            _t = token.translate(str.maketrans("", "", string.digits)).strip()
            if _t and not _t.isspace():
                yield _t

    def lowercase(self, tokens: Iterator[str]) -> Iterator[str]:
        for token in tokens:
            yield token.lower()

    def stopwords(self, tokens: Iterator[str]) -> Iterator[str]:
        for token in tokens:
            if token not in self._stopwords:
                yield token
