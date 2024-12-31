camel = input("camelCase: ")
snake = ""

for letter in camel:
    if letter.isupper():
        new_letter = "_" + letter.lower()
        snake = snake + new_letter
    else:
        snake = snake + letter

print("snake_case:", snake)

##ALTERNATIVE WITH JUST PRINTING EVERYTIME INSTEAD OF ADDING TO A PREEXISTING STRING
#camel = input("camelCase: ")

#for letter in camel:
#    if letter.isupper():
#        print("_" + letter.lower(), end = "")
#    else:
#        print(letter, end = "")

#print("\r")
