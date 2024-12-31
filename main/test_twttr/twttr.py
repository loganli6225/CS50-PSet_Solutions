def main():
    input_string = input("Input: ")
    print(shorten(input_string))


def shorten(word):
    output_string = ""
    for letter in word:
        if letter.lower() == "a" or letter.lower() == "e" or letter.lower() == "i" or letter.lower() == "o" or letter.lower() == "u":
            output_string
        else:
            output_string += letter
    return output_string

# def shorten(word):
#     word = word.replace("a", "")
#     word = word.replace("e", "")
#     word = word.replace("i", "")
#     word = word.replace("o", "")
#     word = word.replace("u", "")
#     word = word.replace("A", "")
#     word = word.replace("E", "")
#     word = word.replace("I", "")
#     word = word.replace("O", "")
#     word = word.replace("U", "")
#     return word


if __name__ == "__main__":
    main()
