from twttr import shorten


def test_shorten():
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""
    assert shorten("twitter") == "twttr"
    assert shorten("tWitTer") == "tWtTr"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("1a2be") == "12b"
