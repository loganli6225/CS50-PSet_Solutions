def main():
    perc = math_perc()
    if perc <= 1:
        print("E")
    elif perc >= 99:
        print("F")
    else:
        print(perc, "%", sep ="")

def math_perc():
    while True:
        try:
            x, y = input("Fraction: ").split("/")
            int(x)/int(y)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            if int(x)/int(y) <= 1:
                return round(((int(x)/int(y))*100))

main()

