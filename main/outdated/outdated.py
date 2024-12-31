list_of_months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    print(function())

def function():
    while True:
        input_date = input("Date: ")
        try: # Check Format of 9/8/1636 part 1
            month, day, year = input_date.split("/") # ValueError if not two / --> three parts
            month = int(month) # ValueError if month not an integer (checks for no added characters in month)
            day = int(day) # ValueError if day not an integer (checks for no added non-integer characters in day)
            year = int(year) # ValueError if year not an integer (checks for no added characters in year)
        except ValueError: # if ValueError ...
            try: # Check format of September 8, 1636 part 1
                month, day, year = input_date.split(" ") # ValueError if not two spaces --> three parts
                month = list_of_months.index(month) + 1 # ValueError if month isn't in list_of_months (checks for no added characters in month)
                int(day.replace(",", "")) # ValueError if day (w/o commas) isn't an integer (checks for no added non-integer characters in day)
                year = int(year) # ValueError if year not an integer (checks for no added characters in year)
            except ValueError:
                pass
            else: # Check format of September 8, 1636 part 2
                if 0 <= year <= 9999 and day.count(",") == 1 and day.find(",") == len(day)-1 and 1 <= int(day.replace(",", "")) <= 31: # Checks if year is valid date value, if only one comma in day-term, if the one comma is at the end of the day-term, and if day is valid date value
                    day = int(day.replace(",", ""))
                    return f"{year:04}-{month:02}-{day:02}"
                else:
                    pass
        else: # Check Format of 9/8/1636 part 2
            if 1 <= month <= 12 and 1 <= day <= 31 and 0 <= year <= 9999: # Check Month, Day, and Year are all valid date values
                return f"{year:04}-{month:02}-{day:02}"
            else:
                pass

main()
