from invertedIndex.tokenize.base import Tokenizer


class FrenchTokenizer(Tokenizer):
    def get_stopword_file_path(self) -> str:
        return "stopwords_fr.txt"
