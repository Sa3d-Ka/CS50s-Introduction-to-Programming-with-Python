import random


def main():
    level = get_level()
    score = simulate_game(level)
    print("Score:", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3 :
                break
        except ValueError:
            pass
    return level

def generate_integer(level):
    if level == 1:
        x = random.randint(0, 10)
        y = random.randint(0, 10)
        return x, y
    elif level == 2:
        x = random.randint(10, 50)
        y = random.randint(10, 50)
        return x, y
    elif level == 3:
        x = random.randint(50, 99)
        y = random.randint(50, 99)
        return x, y
    

def simulate_round(x, y):
    tries = 1
    while tries <= 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == x+y:
                return True
            else:
                tries += 1
                print("EEE")
        except:
            tries += 1
            print("EEE")
    print(f"{x} + {y} = {x + y}")
    return False


def simulate_game(level):
    score = 0
    i = 1
    while i <= 10:
        x, y = generate_integer(level)
        responce = simulate_round(x, y)
        if responce == True:
            score += 1
        i += 1
    return score
            


if __name__ == "__main__":
    main()