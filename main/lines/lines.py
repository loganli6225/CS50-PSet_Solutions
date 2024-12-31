import sys

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command line arguments")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")
else:
    try:
        open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File Does Not Exist")
    else:
        i = 0
        with open(sys.argv[1]) as file:
            for line in file:
                if not line.lstrip().startswith("#") and not line.isspace():
                    i += 1
        print(i)
