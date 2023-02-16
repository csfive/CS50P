from datetime import date
from seasons import get_total_minutes


def test_get_minutes():
    assert get_total_minutes(date(1999, 1, 1), date(2000, 1, 1)) == 525600
    assert get_total_minutes(date(2001, 1, 1), date(2003, 1, 1)) == 1051200
    assert get_total_minutes(date(1995, 1, 1), date(2000, 1, 1)) == 2629440
    assert get_total_minutes(date(2020, 6, 1), date(2032, 1, 1)) == 6092640
