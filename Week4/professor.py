from random import randint


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        score += check_answer(x, y)
    print("Score:", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return randint(0, 9)
    return randint(10 ** (level - 1), 10**level - 1)


def check_answer(x, y):
    tries = 0
    while tries < 3:
        try:
            tries += 1
            answer = int(input(f"{x} + {y} = "))
            if answer == x + y:
                return 1
            else:
                print("EEE")
        except ValueError:
            pass
    print(f"{x} + {y} = {x + y}")
    return 0


if __name__ == "__main__":
    main()
