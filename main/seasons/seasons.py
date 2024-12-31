from datetime import date
import sys
import inflect


def main():
    print(mins_from(input("Date of Birth: ")))

def mins_from(start_date):
    try:
        birth = date.fromisoformat(start_date)
    except ValueError:
        sys.exit("Invalid Date")
    else:
        today = date.today()
        difference = today - birth
        mins = difference.days * 24 * 60

        p = inflect.engine()
        words = p.number_to_words(mins).replace(" and ", " ")
        return (f"{words.capitalize()} minutes")

if __name__ == "__main__":
    main()
