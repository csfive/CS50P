import csv
import sys

if len(sys.argv) != 3 or not sys.argv[1].endswith(".csv"):
    sys.exit("Invalid arguments.")

try:
    with open(sys.argv[1]) as input, open(sys.argv[2], "w", newline="") as output:
        reader = csv.DictReader(input)
        writer = csv.DictWriter(output, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in reader:
            last_name, first_name = row["name"].strip().split(", ")
            writer.writerow(
                {"first": first_name, "last": last_name, "house": row["house"]}
            )

except FileNotFoundError:
    sys.exit("File does not exist.")
