def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    if not all(ch.isalnum() for ch in s):
        return False

    flag = False
    for ch in s:
        if ch.isdigit():
            flag = True
        if ch.isalpha() and flag:
            return False

    for ch in s:
        if ch.isdigit():
            return ch != "0"

    return True


if __name__ == "__main__":
    main()
