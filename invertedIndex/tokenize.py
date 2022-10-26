import string
from typing import Iterator


class Tokenizer:
    def __init__(self, delimiter=" "):
        self.delimiter = delimiter

    def analyze(self, term: str) -> Iterator[str]:
        tokens = self.split(term)
        for apply_func in (self.remove_punctation, self.text_only, self.lowercase):
            tokens = apply_func(tokens)
        yield from tokens

    def split(self, term: str) -> Iterator[str]:
        for token in term.split(self.delimiter):
            yield token

    def remove_punctation(self, tokens: Iterator[str]) -> Iterator[str]:
        for token in tokens:
            yield token.translate(str.maketrans("", "", string.punctuation))

    def text_only(self, tokens: Iterator[str]) -> Iterator[str]:
        for token in tokens:
            if token.isalpha():
                yield token

    def lowercase(self, tokens: Iterator[str]) -> Iterator[str]:
        for token in tokens:
            yield token.lower()
