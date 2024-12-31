def main():
    string = input()
    newstring = convert(string)
    print(newstring)

def convert(string):
    string1 = string.replace(":)", "🙂")
    string2 = string1.replace(":(", "🙁")
    return string2

main()
