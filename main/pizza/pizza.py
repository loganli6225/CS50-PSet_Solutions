import sys
import csv
from tabulate import tabulate

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")
else:
    try:
        open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File Does Not Exist")
    else:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            print(tabulate(reader, headers = "firstrow", tablefmt="grid"))

