from tabulate import tabulate
import sys
import csv


if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)
elif not sys.argv[1].endswith(".csv"):
    print("Not a CSV file")
    sys.exit(1)


try:
    file_name = sys.argv[1]
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        table = list(reader)

        headers = table[0]
        data = table[1:]

        print(tabulate(data, headers, tablefmt="grid"))

except FileNotFoundError:
    print(f"File does not exist")
    sys.exit(1)