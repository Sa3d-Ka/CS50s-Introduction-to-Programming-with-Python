amount = 50

while amount > 0:
    print("Amount Due:", amount)
    coins = int(input("Insert coin: "))
    if coins in [25, 10, 5]:
        amount -= coins
    else:
        print("Invalid coin. Please insert 25, 10, or 5 cents.")

print("Change Owed:", -amount)
