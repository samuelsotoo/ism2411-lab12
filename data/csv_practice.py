("--- Exercise 1-4 ---")

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
    
    
("--- Exercise 5 ---")
total_rows = 0
written_rows = 0

with open("data/sales.csv", newline="") as infile, open("data/cleaned.csv", "w", newline="") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    next(reader) # skip the original header
    writer.writerow(["Product", "Price", "Qty", "Total"])

    for row in reader:
        total_rows += 1
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        order_total = price * quantity

        if order_total > 100:
            writer.writerow([product, f"{price:.2f}", quantity, f"{order_total:.2f}"])
            written_rows += 1


print(f"Rows written: {written_rows}")
print(f"Rows in original: {total_rows}")
