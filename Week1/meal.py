def main():
    time = convert(input("What time is it? ").strip())
    if 7 <= time <= 8:
        print("Breakfast time")
    elif 12 <= time <= 13:
        print("Lunch time")
    elif 18 <= time <= 19:
        print("Dinner time")


def convert(time):
    hours, minutes = map(int, time.replace("a.m.", "").replace("p.m.", "").split(":"))
    if "p.m." in time and hours != 12:
        hours += 12
    if "a.m." in time and hours == 12:
        hours = 0
    return hours + minutes / 60


if __name__ == "__main__":
    main()
