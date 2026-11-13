("--- Exercise 1-4 ---")

import csv
from datetime import datetime

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

("--- Exercise 6 ---")
# csv.reader uses column positions like row[1], which is quick but breaks if the column order changes, so I'd use it for small files with a fixed layout
# csv.DictReader uses names like row["price"], which is easier to read and safer when columns move, so I'd use it for bigger files or code other people will read.

dict_rows = 0
dict_over_100 = 0
dict_revenue = 0

with open("data/sales.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        dict_rows += 1
        price = float(row["price"])
        quantity = int(row["quantity"])
        order_total = price * quantity
        dict_revenue += order_total
        if order_total > 100:
            dict_over_100 += 1

print(f"Rows read: {dict_rows}")
print(f"Orders over $100: {dict_over_100}")
print(f"Total revenue: ${dict_revenue:.2f}")

("--- Exercise 7 ---")
summary = {}

with open("data/sales.csv", newline="") as f:
     reader = csv.DictReader(f)
     for row in reader:
          name = row["product"]
          revenue = float(row["price"]) * int(row["quantity"])
          summary[name] = summary.get(name, 0) + revenue 

for name in sorted(summary):
     print(f"{name}: ${summary[name]:.2f}")

("--- Exercise 8 ---")
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("data/run_log.txt", "a") as log:
     log.write(f"{timestamp} - Total revenue: ${total:.2f}\n")
     