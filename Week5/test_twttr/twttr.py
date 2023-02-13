def main():
    print("Output:", shorten(input("Input: ")))


def shorten(word):
    return "".join([ch for ch in word if ch.lower() not in "aeiou"])


if __name__ == "__main__":
    main()
