# flake8: noqa
import unittest

from invertedIndex.tokenizer import Tokenizer


class TokenizerTest(unittest.TestCase):
    def setUp(self):
        self.tokenizer = Tokenizer()
        self.tokenizer_with_pipe_delimiter = Tokenizer("|")

    # region Tokenize test
    def test_tokenize_with_default_tokenizer(self):
        assert list(self.tokenizer.tokenize("Hello world")) == ["Hello", "world"]

    def test_tokenize_with_pipe_tokenizer(self):
        assert list(self.tokenizer_with_pipe_delimiter.tokenize("Hello world")) == [
            "Hello world"
        ]
        assert list(self.tokenizer_with_pipe_delimiter.tokenize("Hello|world")) == [
            "Hello",
            "world",
        ]

    # endregion

    # region Remove Punctuation test
    def test_remove_punctuation(self):
        tokens = self.tokenizer.tokenize("Hello world")
        complex_tokens = self.tokenizer.tokenize("!hi. wh?at is the weat[h]er lik?e.")
        assert list(self.tokenizer.remove_punctuation(tokens)) == ["Hello", "world"]
        assert list(self.tokenizer.remove_punctuation(complex_tokens)) == [
            "hi",
            "what",
            "is",
            "the",
            "weather",
            "like",
        ]

    # endregion

    # region normalize test
    def test_normalize(self):
        tokens = self.tokenizer.tokenize("Hello world")
        tokens_with_accents = self.tokenizer.tokenize(
            "C'est l'instant où le malade qui a été obligé de partir en voyage et a dû coucher dans un hôtel inconnu, "
            "réveillé par une crise, se réjouit en apercevant sous la porte une raie de jour"
        )
        expected_tokens_with_accents = [
            "C'est",
            "l'instant",
            "ou",
            "le",
            "malade",
            "qui",
            "a",
            "ete",
            "oblige",
            "de",
            "partir",
            "en",
            "voyage",
            "et",
            "a",
            "du",
            "coucher",
            "dans",
            "un",
            "hotel",
            "inconnu,",
            "reveille",
            "par",
            "une",
            "crise,",
            "se",
            "rejouit",
            "en",
            "apercevant",
            "sous",
            "la",
            "porte",
            "une",
            "raie",
            "de",
            "jour",
        ]
        assert list(self.tokenizer.normalize(tokens)) == ["Hello", "world"]
        assert (
            list(self.tokenizer.normalize(tokens_with_accents))
            == expected_tokens_with_accents
        )

    # endregion

    # region text only test
    def test_text_only(self):
        tokens = self.tokenizer.tokenize("Hello world")
        tokens_with_digits = self.tokenizer.tokenize("I have 235 dollars in my pocket")
        tokens_with_digits_full = self.tokenizer.tokenize("3456789")
        assert list(self.tokenizer.text_only(tokens)) == ["Hello", "world"]
        assert list(self.tokenizer.text_only(tokens_with_digits)) == [
            "I",
            "have",
            "dollars",
            "in",
            "my",
            "pocket",
        ]
        assert list(self.tokenizer.text_only(tokens_with_digits_full)) == []

    # endregion

    # region lowercase
    def test_lowercase(self):
        tokens = self.tokenizer.tokenize("Hello world")
        tokens_randomize = self.tokenizer.tokenize("hi WHaT iS THE WEAtHeR LikE")
        assert list(self.tokenizer.lowercase(tokens)) == ["hello", "world"]
        assert list(self.tokenizer.lowercase(tokens_randomize)) == [
            "hi",
            "what",
            "is",
            "the",
            "weather",
            "like",
        ]

    # endregion

    # region stopwords
    def test_french_stopwords(self):
        tokens_without_stopwords = self.tokenizer.tokenize("Bonjour")
        tokens_with_stopwords = self.tokenizer.tokenize(
            "C'est l'instant où le malade qui a été obligé de partir en voyage et a dû coucher dans un hôtel inconnu, "
            "réveillé par une crise, se réjouit en apercevant sous la porte une raie de jour"
        )
        expected_tokens_with_stopwords = [
            "C'est",
            "l'instant",
            "malade",
            "obligé",
            "partir",
            "voyage",
            "dû",
            "coucher",
            "hôtel",
            "inconnu,",
            "réveillé",
            "crise,",
            "réjouit",
            "apercevant",
            "porte",
            "raie",
            "jour",
        ]
        assert list(self.tokenizer.stopwords(tokens_without_stopwords)) == ["Bonjour"]
        assert (
            list(self.tokenizer.stopwords(tokens_with_stopwords))
            == expected_tokens_with_stopwords
        )

    # endregion

    # region analyze
    def test_analyze(self):
        sentence = "Bonjour tout le moNde."
        big_sentence = """C'est l'instant où le malade qui a été obligé de partir en voyage et a dû coucher dans un hôtel inconnu, 
            réveillé par une crise, se réjouit en apercevant sous la porte une raie de jour
        """
        expected_big_sentence = [
            "cest",
            "linstant",
            "malade",
            "ete",
            "oblige",
            "partir",
            "voyage",
            "coucher",
            "hotel",
            "inconnu",
            "reveille",
            "crise",
            "rejouit",
            "apercevant",
            "porte",
            "raie",
        ]
        assert list(self.tokenizer.analyze(sentence)) == ["bonjour", "monde"]
        assert list(self.tokenizer.analyze(big_sentence)) == expected_big_sentence

    # endregion
