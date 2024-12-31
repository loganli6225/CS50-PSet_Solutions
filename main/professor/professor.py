import random


def main():
    level = get_level()
    list_of_cor_incor = []
    for prob_num in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        cor_incor = generate_problem(x, y)
        list_of_cor_incor.append(cor_incor)
    print(f"Score: {list_of_cor_incor.count("Correct")}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1 or level > 3:
                raise ValueError
        except ValueError:
            pass
        else:
            return level


def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    elif level == 3:
        return random.randint(100,999)
    else:
        raise ValueError

def generate_problem(x, y):
    answer = x + y
    for i in range(3):
        try:
            user_answer = int(input(f"{x} + {y} = "))
            if answer != user_answer:
                raise ValueError
        except ValueError:
            print("EEE")
            pass
        else:
            return "Correct"
    print(f"{x} + {y} = {answer}")
    return "Incorrect"


if __name__ == "__main__":
    main()
