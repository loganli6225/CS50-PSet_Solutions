import random

while True:
    try:
        l = int(input("Level: "))
    except ValueError:
        pass
    else:
        if l < 1:
            pass
        else:
            n = random.randint(1, l)
            break

while True:
    try:
        g = int(input("Guess: "))
    except ValueError:
        pass
    else:
        if g < 1:
            pass
        else:
            if g < n:
                print("Too small!")
            elif g > n:
                print("Too large!")
            else:
                print("Just Right!")
                break
