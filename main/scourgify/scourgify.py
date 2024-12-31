import sys
import csv


if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command line arguments")


if not sys.argv[1].endswith(".csv") and not sys.argv[2].endswith(".csv"):
    sys.exit("Input File and Output File Not CSV files")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Input File Not a CSV file")
elif not sys.argv[2].endswith(".csv"):
    sys.exit("Output File Not a CSV file")


try:
    open(sys.argv[1])
except FileNotFoundError:
    sys.exit("Could not read", sys.argv[1])
else:
    students = []
    with open(sys.argv[1]) as file_one:
        reader = csv.DictReader(file_one)
        for row in reader:
            last, first = row["name"].split(",")
            first = first.strip()
            students.append({"first": first, "last": last, "house": row["house"]})

with open(sys.argv[2], "w") as file_two:
    writer = csv.DictWriter(file_two, fieldnames = ["first", "last", "house"])
    writer.writeheader()
    for student in students:
        writer.writerow(student)
