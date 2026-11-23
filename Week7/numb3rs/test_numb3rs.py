from numb3rs import validate


def test_validate():
    assert validate("275.3.6.28") == False
    assert validate("hello") == False
    assert validate("10.0.10") == False
    assert validate("192.168.1.1.1") == False
    assert validate("255.256.256.256") == False

    assert validate("192.168.1.1") == True
    assert validate("10.0.0.1") == True
    assert validate("172.16.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True


def test_leading_zeros():
    # A lone 0 is an octet; a 0 in front of other digits is not.
    assert validate("000.001.010.100") == False
    assert validate("01.2.3.4") == False
    assert validate("1.2.3.04") == False
    assert validate("1.00.3.4") == False


def test_non_ascii_digits():
    # Python's \d also matches digits from other scripts, such as "٩".
    assert validate("1٩٢.168.1.1") == False
    assert validate("١.2.3.4") == False
