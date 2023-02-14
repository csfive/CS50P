import sys

if len(sys.argv) != 2 or not sys.argv[1].endswith(".py"):
    sys.exit("Invalid arguments.")

try:
    with open(sys.argv[1]) as file:
        print(
            sum(
                1 for line in file if line.strip() and not line.lstrip().startswith("#")
            )
        )
except FileNotFoundError:
    sys.exit("File does not exist.")
