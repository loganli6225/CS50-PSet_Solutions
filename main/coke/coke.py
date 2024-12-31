need = 50

while need > 0:
    while True:
        print("Amount Due:", need)
        amt = int(input("Insert Coin: "))
        if amt == 25 or amt == 10 or amt == 5:
            break
    need -= amt

print("Change Owed:", need * -1)
