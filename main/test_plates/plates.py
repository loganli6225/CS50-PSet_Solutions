def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return is_length(s) and is_two_letters(s)and is_two_letters(s) and is_Alpha_or_Numeric(s) and is_numbers_last(s) and is_first_zero(s)


def is_length(string):
    return 2 <= len(string) <= 6

def is_two_letters(string):
    first_two = string[0:2]
    return first_two.isalpha()

def is_numbers_last(string):
    for i in string:
        if i.isnumeric():
            place = string.find(i)
            end_string = string[place:len(string)]
            return end_string.isnumeric()
    return True

def is_first_zero(string):
    for i in string:
        if i.isnumeric():
            return i != "0"
    return True

def is_Alpha_or_Numeric(string):
    return string.isalnum()

if __name__ == "__main__":
    main()
