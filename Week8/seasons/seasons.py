from datetime import date
import inflect
import sys


def get_total_minutes(birth_date, today):
    return (today - birth_date).days * 24 * 60


def main():
    try:
        birth_date = date.fromisoformat(input("Date of Birth: "))
    except ValueError:
        sys.exit("Invalid input.")

    total_minutes = get_total_minutes(birth_date, date.today())
    p = inflect.engine()
    print(
        f"{p.number_to_words(total_minutes, andword='').capitalize()} {p.plural('minute', total_minutes)}"
    )


if __name__ == "__main__":
    main()
