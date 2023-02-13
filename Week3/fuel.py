while True:
    try:
        x, y = map(int, input("Fraction: ").split("/"))
        if y == 0:
            raise ZeroDivisionError
        if x > y:
            raise ValueError
        break
    except (ValueError, ZeroDivisionError):
        pass

percentage = round(x / y * 100)
if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage}%")
