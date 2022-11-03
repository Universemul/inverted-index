from invertedIndex.tokenize.base import Tokenizer


class EnglishTokenizer(Tokenizer):
    def get_stopword_file_path(self) -> str:
        return "stopwords_en.txt"
