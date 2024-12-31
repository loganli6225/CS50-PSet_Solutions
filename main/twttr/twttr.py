##ALTERNATIVE VERSION WITH JUST PRINTING EVERYTIME INSTEAD OF ADDING TO A PREEXISTING STRING
#def main():
#    input_string = input("Input: ")
#    print("Output: ", end = "")
#    for letter in input_string:
#        if is_vowel(letter):
#            continue
#        else:
#            print(letter, end = "")
#    print("\r")

def main():
    input_string = input("Input: ")
    output_string = ""
    for letter in input_string:
        if is_vowel(letter):
            output_string
        else:
            output_string += letter
    print("Output:", output_string)

def is_vowel(letter):
    return letter.lower() == "a" or letter.lower() == "e" or letter.lower() == "i" or letter.lower() == "o" or letter.lower() == "u"

main()
