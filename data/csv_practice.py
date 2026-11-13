("--- Exercise 2 ---")

import csv

with open("data/sales.csv", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)
    print(header)  # Skip the header row
   
    total = 0
    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        revenue = price * quantity
        total += revenue
        print(f"{product}: {quantity} units * ${price:.2f} = ${revenue:.2f}")

    print(f"Total revenue: ${total:.2f}")

