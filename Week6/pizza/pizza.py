from tabulate import tabulate
import csv
import sys

if len(sys.argv) != 2 or not sys.argv[1].endswith(".csv"):
    sys.exit("Invalid arguments.")

try:
    with open(sys.argv[1]) as file:
        print(tabulate(csv.DictReader(file), headers="keys", tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist.")
