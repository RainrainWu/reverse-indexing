import pytest

from analyzer.tokenizer import Tokenizer


@pytest.mark.parametrize(
    "file,tokens",
    [
        ("example, text file,for test", ["example,", "text", "file,for", "test"])
    ]
)
def test_tokenize_by_blank(file, tokens):
    t = Tokenizer()
    t.load(file).tokenize_by_blank()
    assert t.extract() == tokens


@pytest.mark.parametrize(
    "file,tokens",
    [
        ("example, text file,for test", ["example", " text file", "for test"])
    ]
)
def test_tokenize_by_comma(file, tokens):
    t = Tokenizer()
    t.load(file).tokenize_by_comma()
    assert t.extract() == tokens
