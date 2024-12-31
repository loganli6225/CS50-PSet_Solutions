#def main():
#    time = input("What time is it? ")
#    numtime = convert(time)
#    if 7 <= numtime <= 8:
#        print("breakfast time")
#    elif 12 <= numtime <= 13:
#        print("lunch time")
#    elif 18 <= numtime <= 19:
#        print("dinner time")
#    else:
#        return

#def convert(time):
#    first, last = time.split(":")
#    first = int(first)
#    last = int(last)/60
#    return first + last

#if __name__ == "__main__":
#    main()

##IMPROVED VERSION COMPATIBLE WITH 12 HOUR AND 24 HOUR
def main():
    time = input("What time is it? ")
    if time.endswith("a.m."):
        time_new = time.removesuffix("a.m.")
        numtime = convert(time_new)
        if 7 <= numtime <= 8:
            print("breakfast time")
        else:
            return
    elif time.endswith("p.m."):
        time_new = time.removesuffix("p.m.")
        numtime = convert(time_new)
        if 12 <= numtime <= 13:
            print("lunch time")
        elif 6 <= numtime <= 7:
            print("dinner time")
        else:
            return
    else:
        numtime = convert(time)
        if 7 <= numtime <= 8:
            print("breakfast time")
        elif 12 <= numtime <= 13:
            print("lunch time")
        elif 18 <= numtime <= 19:
            print("dinner time")
        else:
            return

def convert(time):
    first, last = time.split(":")
    first = int(first)
    last = int(last)/60
    return first + last

if __name__ == "__main__":
    main()
