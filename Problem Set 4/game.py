import random

while True:
    try:
        level = int(input("Level: "))
        if level > 1:
            break
    except ValueError:
        pass

rand_num = random.randrange(1, level)


while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess > rand_num:
                print("Too large!")
            elif guess < rand_num:
                print("Too small!")
            else:
                print("Just right!")
                break
    except ValueError:
        pass
