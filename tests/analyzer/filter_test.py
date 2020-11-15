import pytest

from analyzer.filter import Filter


@pytest.mark.parametrize(
    "stream,output",
    [
        (
            ["EXAMPLE", "TokenStream", "for", "Test"],
            ["example", "tokenstream", "for", "test"]
        )
    ]
)
def test_filter_lower(stream, output):
    f = Filter()
    f.load(stream).filter_lower()
    assert f.extract() == output


@pytest.mark.parametrize(
    "stream,output",
    [
        (
            ["EXAMPLE", "TokenStream", "for", "Test"],
            ["EXAMPLE", "TOKENSTREAM", "FOR", "TEST"]
        )
    ]
)
def test_filter_upper(stream, output):
    f = Filter()
    f.load(stream).filter_upper()
    assert f.extract() == output


@pytest.mark.parametrize(
    "stream,output",
    [
        (
            [u"EXAMPLE\xe5", u"\xb7TokenStream", u"f\xc6or", u"Test\xa4"],
            ["EXAMPLE", "TokenStream", "for", "Test"]
        )
    ]
)
def test_filter_ascii(stream, output):
    f = Filter()
    f.load(stream).filter_ascii()
    assert f.extract() == output
