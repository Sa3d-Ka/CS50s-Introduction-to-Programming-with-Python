from tabulate import tabulate
import sys
import csv
import os

table = []
headers = ["Regular Pizza", "Small", "Large"]

if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)
else:
    file_name = sys.argv[1]  # Use the file path provided by the user

    # Check if the file is a CSV file
    if not file_name.endswith(".csv"):
        print("Not a CSV file")
        sys.exit(1)

    # Check if the file exists
    if not os.path.exists(file_name):
        print("File does not exist")
        sys.exit(1)

    # Process the CSV file
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            table.append([row['Regular Pizza'], row['Small'], row['Large']])

    print(tabulate(table, headers, tablefmt="grid"))