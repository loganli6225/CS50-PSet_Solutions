x, y, z = input("Expression: ").split()
x = int(x)
z = int(z)

match y:
    case "+":
        print(round(float(x+z), 1))
    case "-":
        print(round(float(x-z), 1))
    case "*":
        print(round(float(x*z), 1))
    case "/":
        print(round(float(x/z), 1))
