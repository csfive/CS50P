from um import count


def test_count():
    assert count("hello world") == 0
    assert count("yummy") == 0
    assert count("umum") == 0

    assert count("hello, um, world") == 1
    assert count("um um um") == 3
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
