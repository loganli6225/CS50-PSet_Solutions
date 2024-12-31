menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total_price_str = 0


while True:
    try:
        item = input("Item: ").title()
        total_price_num = float(total_price_str) + menu[item]
    except KeyError:
        pass
    except EOFError:
        print("\r")
        break
    else:
        total_price_str = str(total_price_num)
        before, after = total_price_str.split(".")
        if len(after) == 1:
            total_price_str = total_price_str + "0"
        print(f"Total: ${total_price_str}")
