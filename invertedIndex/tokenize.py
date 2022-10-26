import string
import typing


class Tokenizer:

    def __init__(self, delimiter=' '):
        self.delimiter = delimiter

    def analyze(self, term: str) -> typing.Iterator[str]:
        tokens = self.split(term)
        for apply_func in (self.remove_punctation, self.text_only, self.lowercase):
            tokens = apply_func(tokens)
        yield from tokens

    def split(self, term: str) -> typing.Iterator[str]:
        for token in term.split(self.delimiter):
            yield token

    def remove_punctation(self, tokens: typing.Iterator[str]) -> typing.Iterator[str]:
        for token in tokens:
            yield token.translate(str.maketrans('', '', string.punctuation))

    def text_only(self, tokens: typing.Iterator[str]) -> typing.Iterator[str]:
        for token in tokens:
            if token.isalpha():
                yield token

    def lowercase(self, tokens: typing.Iterator[str]) -> typing.Iterator[str]:
        for token in tokens:
            yield token.lower()
