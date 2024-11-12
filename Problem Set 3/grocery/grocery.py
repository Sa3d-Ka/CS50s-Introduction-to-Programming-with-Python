grocery = {}

while True:
    try:
        items = input().lower()
        if items in grocery:
            grocery[items] += 1
        else:
            grocery[items] = 1
    except EOFError:
        for key in sorted(grocery.keys()):
            print(grocery[key], key.upper())
        break