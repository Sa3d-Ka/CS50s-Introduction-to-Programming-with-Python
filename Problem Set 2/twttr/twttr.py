inp = input("Input: ")
print("Output: ", end="")

for letter in inp:
    if not letter.lower() in ['a', 'e', 'i', 'o', 'o']:
        print(letter, end="")
print()