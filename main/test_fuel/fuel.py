def main():
    frac = input("Fraction: ")
    perc = convert(frac)
    print(gauge(perc))

def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            int(x)/int(y)
            if int(x) > int(y):
                raise ValueError
        except (ValueError, ZeroDivisionError):
            pass
        else:
            return round(((int(x)/int(y))*100))

def gauge(percentage):
    if percentage <= 1:
        return f"E"
    elif percentage >= 99:
        return f"F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
