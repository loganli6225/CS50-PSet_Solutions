import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    if matches := re.search(r"^(?:((?:[1][0-2])|(?:[0-9]))(?::([0-5][0-9]))?) (AM|PM) to (?:((?:[1][0-2])|(?:[0-9]))(?::([0-5][0-9]))?) (AM|PM)$", s, re.IGNORECASE):
        hours = [matches.group(1), matches.group(4)]
        mins = [matches.group(2), matches.group(5)]
        periods = [matches.group(3), matches.group(6)]

        for i in range(2):
            if periods[i] == "AM" and hours[i] == "12":
                hours[i] = 0
            elif periods[i] == "PM" and hours[i] != "12":
                hours[i] = int(hours[i]) + 12
            if mins[i] == None:
                mins[i] = 0

        return f"{int(hours[0]):02}:{int(mins[0]):02} to {int(hours[1]):02}:{int(mins[1]):02}"

    else:
        raise ValueError


if __name__ == "__main__":
    main()
