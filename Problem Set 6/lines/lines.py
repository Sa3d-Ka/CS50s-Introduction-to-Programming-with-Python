import sys

if len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)
elif len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)
elif not sys.argv[1].endswith(".py"):
        print("Not a Python file")
        sys.exit(1)
else:
    try:
        with open(sys.argv[1], 'r') as file:
            reader = file.readlines()
            i = 0
            for line in reader:
                if not "#" in line and not line.isspace():
                     i += 1
            print(i)
    except FileNotFoundError:
         print("File does not exist")
        