import inflect
p = inflect.engine()
list_names = []


while True:
    try:
        name = input("Name: ")
    except EOFError:
        break
    else:
        list_names.append(name)

all_names = p.join(list_names[0:len(list_names)])
print("Adieu, adieu, to", all_names)
