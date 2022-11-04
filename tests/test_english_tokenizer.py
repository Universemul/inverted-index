# flake8: noqa
import unittest

from invertedIndex.tokenize.english import EnglishTokenizer


class TokenizerTest(unittest.TestCase):
    def setUp(self):
        self.basic_sentence = "Hello world"
        self.basic_sentence_pipe = "Hello|world"
        self.tokenizer = EnglishTokenizer()
        self.tokenizer_with_pipe_delimiter = EnglishTokenizer("|")

    # region Tokenize test
    def test_tokenize_with_default_tokenizer(self):
        assert list(self.tokenizer.tokenize(self.basic_sentence)) == [
            "Hello",
            "world",
        ]

    def test_tokenize_with_pipe_tokenizer(self):
        assert list(
            self.tokenizer_with_pipe_delimiter.tokenize(self.basic_sentence)
        ) == ["Hello world"]
        assert list(
            self.tokenizer_with_pipe_delimiter.tokenize(self.basic_sentence_pipe)
        ) == [
            "Hello",
            "world",
        ]

    # endregion

    # region Remove Punctuation test
    def test_remove_punctuation(self):
        tokens = self.tokenizer.tokenize(self.basic_sentence)
        complex_tokens = self.tokenizer.tokenize(
            "!Hi. wha?ts the we!at?her like, toda[##}y.[?"
        )
        assert list(self.tokenizer.remove_punctuation(tokens)) == [
            "Hello",
            "world",
        ]
        assert list(self.tokenizer.remove_punctuation(complex_tokens)) == [
            "Hi",
            "whats",
            "the",
            "weather",
            "like",
            "today",
        ]

    # endregion

    # region normalize test
    def test_normalize(self):
        tokens = self.tokenizer.tokenize(self.basic_sentence)
        tokens_with_accents = self.tokenizer.tokenize(
            "It is the moment when the patient who has been obliged to go on a trip and has had to sleep in an unknown hotel, awakened by a crisis, rejoices when he sees a ray of daylight under the door."
        )
        expected_tokens_with_accents = [
            "It",
            "is",
            "the",
            "moment",
            "when",
            "the",
            "patient",
            "who",
            "has",
            "been",
            "obliged",
            "to",
            "go",
            "on",
            "a",
            "trip",
            "and",
            "has",
            "had",
            "to",
            "sleep",
            "in",
            "an",
            "unknown",
            "hotel,",
            "awakened",
            "by",
            "a",
            "crisis,",
            "rejoices",
            "when",
            "he",
            "sees",
            "a",
            "ray",
            "of",
            "daylight",
            "under",
            "the",
            "door.",
        ]
        assert list(self.tokenizer.normalize(tokens)) == ["Hello", "world"]
        assert (
            list(self.tokenizer.normalize(tokens_with_accents))
            == expected_tokens_with_accents
        )

    # endregion

    # region text only test
    def test_text_only(self):
        tokens = self.tokenizer.tokenize(self.basic_sentence)
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
        tokens = self.tokenizer.tokenize(self.basic_sentence)
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
    def test_stopwords(self):
        tokens_without_stopwords = self.tokenizer.tokenize("Hello")
        tokens_with_stopwords = self.tokenizer.tokenize(
            "It is the moment when the patient who has been obliged to go on a trip and has had to sleep in an unknown hotel, awakened by a crisis, rejoices when he sees a ray of daylight under the door."
        )
        expected_tokens_with_stopwords = [
            "It",
            "moment",
            "patient",
            "obliged",
            "go",
            "trip",
            "sleep",
            "unknown",
            "hotel,",
            "awakened",
            "crisis,",
            "rejoices",
            "sees",
            "ray",
            "daylight",
            "door.",
        ]
        assert list(self.tokenizer.stopwords(tokens_without_stopwords)) == ["Hello"]
        assert (
            list(self.tokenizer.stopwords(tokens_with_stopwords))
            == expected_tokens_with_stopwords
        )

    # endregion

    # region analyze
    def test_analyze(self):
        sentence = "Hello woRlD"
        big_sentence = "It is the moment when the patient who has been obLiged to go on a trip and has had to sleep in an unknown hotel, awakEned By   a crisis, rejoices when he sees a ray of daylight under the door."
        expected_big_sentence = [
            "moment",
            "patient",
            "obliged",
            "go",
            "trip",
            "sleep",
            "unknown",
            "hotel",
            "awakened",
            "crisis",
            "rejoices",
            "sees",
            "ray",
            "daylight",
            "door",
        ]
        assert list(self.tokenizer.analyze(sentence)) == ["hello", "world"]
        assert list(self.tokenizer.analyze(big_sentence)) == expected_big_sentence

    # endregion
