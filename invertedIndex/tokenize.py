import string
from typing import Callable, Iterator, Set


class Tokenizer:
    _stopword_files = {"fr": "stopwords/stopwords_fr.txt"}

    def __init__(self, delimiter=" ", lang="fr"):
        self.delimiter = delimiter
        self._stopwords = self._load_stopwords(lang)

    def _load_stopwords(self, lang: str) -> Set[str]:
        if lang not in self._stopword_files:
            raise KeyError(
                f"{lang} is not valid. Available languages : {','.join(self._stopword_files.keys())}"
            )
        with open(self._stopword_files[lang], "r") as f:
            return set(f.readlines())

    def analyze(self, term: str) -> Iterator[str]:
        tokens = self.split(term)
        apply_func: Callable[[Iterator[str]], Iterator[str]]
        for apply_func in (
            self.remove_punctuation,
            self.text_only,
            self.lowercase,
            self.stopwords,
        ):
            tokens = apply_func(tokens)
        yield from tokens

    def split(self, term: str) -> Iterator[str]:
        for token in term.split(self.delimiter):
            yield token

    def remove_punctuation(self, tokens: Iterator[str]) -> Iterator[str]:
        for token in tokens:
            yield token.translate(str.maketrans("", "", string.punctuation))

    def text_only(self, tokens: Iterator[str]) -> Iterator[str]:
        for token in tokens:
            if token.isalpha():
                yield token

    def lowercase(self, tokens: Iterator[str]) -> Iterator[str]:
        for token in tokens:
            yield token.lower()

    def stopwords(self, tokens: Iterator[str]) -> Iterator[str]:
        for token in tokens:
            if token not in self._stopwords:
                yield token
