import typing


class Tokenizer:

    def __init__(self, delimiter=' '):
        self.delimiter = delimiter

    def split(self, term: str) -> typing.Iterator[str]:
        return (x for x in term.split(self.delimiter))
