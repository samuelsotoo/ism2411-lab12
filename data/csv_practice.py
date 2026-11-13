import csv

with open("data/sales.csv", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)