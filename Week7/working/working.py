import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match := re.match(
        r"(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)", s
    ):
        st_hour, st_min, st_ap, ed_hour, ed_min, ed_ap = match.groups()

        if st_min is None and ed_min is None:
            st_min, ed_min = 0, 0
        st_hour, st_min, ed_hour, ed_min = map(int, [st_hour, st_min, ed_hour, ed_min])

        if st_ap == "PM" and st_hour != 12:
            st_hour += 12
        elif st_ap == "AM" and st_hour == 12:
            st_hour = 0

        if ed_ap == "PM" and ed_hour != 12:
            ed_hour += 12
        elif ed_ap == "AM" and ed_hour == 12:
            ed_hour = 0

        if (
            not 0 <= st_hour <= 23
            or not 0 <= st_min <= 59
            or not 0 <= ed_hour <= 23
            or not 0 <= ed_min <= 59
        ):
            raise ValueError("Invalid arguments")

        return f"{st_hour:02d}:{st_min:02d} to {ed_hour:02d}:{ed_min:02d}"
    raise ValueError("Invalid arguments")


if __name__ == "__main__":
    main()
