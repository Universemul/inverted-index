# flake8: noqa
import unittest

from invertedIndex.tokenize.french import FrenchTokenizer


class TokenizerTest(unittest.TestCase):
    def setUp(self):
        self.basic_sentence = "Bonjour le monde"
        self.basic_sentence_pipe = "Bonjour|le|monde"
        self.tokenizer = FrenchTokenizer()
        self.tokenizer_with_pipe_delimiter = FrenchTokenizer("|")

    # region Tokenize test
    def test_tokenize_with_default_tokenizer(self):
        assert list(self.tokenizer.tokenize(self.basic_sentence)) == [
            "Bonjour",
            "le",
            "monde",
        ]

    def test_tokenize_with_pipe_tokenizer(self):
        assert list(
            self.tokenizer_with_pipe_delimiter.tokenize(self.basic_sentence)
        ) == ["Bonjour le monde"]
        assert list(
            self.tokenizer_with_pipe_delimiter.tokenize(self.basic_sentence_pipe)
        ) == [
            "Bonjour",
            "le",
            "monde",
        ]

    # endregion

    # region Remove Punctuation test
    def test_remove_punctuation(self):
        tokens = self.tokenizer.tokenize(self.basic_sentence)
        complex_tokens = self.tokenizer.tokenize(
            "!Bonjour. qu?el temps fait-il aujour[?]]dh'?ui."
        )
        assert list(self.tokenizer.remove_punctuation(tokens)) == [
            "Bonjour",
            "le",
            "monde",
        ]
        assert list(self.tokenizer.remove_punctuation(complex_tokens)) == [
            "Bonjour",
            "quel",
            "temps",
            "faitil",
            "aujourdhui",
        ]

    # endregion

    # region normalize test
    def test_normalize(self):
        tokens = self.tokenizer.tokenize(self.basic_sentence)
        tokens_with_accents = self.tokenizer.tokenize(
            "C'est l'instant où le malade qui a été obligé de partir en voyage et a dû coucher dans un hôtel inconnu, réveillé par une crise, se réjouit en apercevant sous la porte une raie de jour"
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
        assert list(self.tokenizer.normalize(tokens)) == ["Bonjour", "le", "monde"]
        assert (
            list(self.tokenizer.normalize(tokens_with_accents))
            == expected_tokens_with_accents
        )

    # endregion

    # region text only test
    def test_text_only(self):
        tokens = self.tokenizer.tokenize(self.basic_sentence)
        tokens_with_digits = self.tokenizer.tokenize("J'ai 235 dollars dans ma poche")
        tokens_with_digits_full = self.tokenizer.tokenize("3456789")
        assert list(self.tokenizer.text_only(tokens)) == ["Bonjour", "le", "monde"]
        assert list(self.tokenizer.text_only(tokens_with_digits)) == [
            "J'ai",
            "dollars",
            "dans",
            "ma",
            "poche",
        ]
        assert list(self.tokenizer.text_only(tokens_with_digits_full)) == []

    # endregion

    # region lowercase
    def test_lowercase(self):
        tokens = self.tokenizer.tokenize(self.basic_sentence)
        tokens_randomize = self.tokenizer.tokenize(
            "HelLo QueL tEmpS fait-IL aujoUrd'HUI"
        )
        assert list(self.tokenizer.lowercase(tokens)) == ["bonjour", "le", "monde"]
        assert list(self.tokenizer.lowercase(tokens_randomize)) == [
            "hello",
            "quel",
            "temps",
            "fait-il",
            "aujourd'hui",
        ]

    # endregion

    # region stopwords
    def test_stopwords(self):
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
            "jour",
        ]
        assert list(self.tokenizer.analyze(sentence)) == ["bonjour", "monde"]
        assert list(self.tokenizer.analyze(big_sentence)) == expected_big_sentence

    # endregion
