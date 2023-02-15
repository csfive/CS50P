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
