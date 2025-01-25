import csv
import sys

if len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit(1)
elif len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)

try:
    liste = []
    with open(sys.argv[1], 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            first, last = row['name'].split(", ")
            liste.append([first, last, row["house"]])
    
    with open(sys.argv[2], 'w', newline='', encoding="utf-8") as file2:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(file2, fieldnames=fieldnames)
        
        writer.writeheader()
        
        for i in liste:
            writer.writerow({"first": i[0], "last": i[1], "house": i[2]})

except FileNotFoundError:
    print("File does not exist")
    sys.exit(1)