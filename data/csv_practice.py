# Question 1: Doing this in Excel would have been faster for a one-time job, since I could filter the orders over $100 and make a pivot table by product in a few clicks and see the results right away. But with Python I can rerun the same steps on any similar CSV just by running the script, and it handles much larger files and keeps a record of its runs, like the log file I appended to. Excel is easier to use for exploring data and making charts, but Python is better for repeating a process automatically without redoing the work by hand
# Question 2: A basketball team’s analytics staff could use an append-mode log to record each player’s minutes and points after every game, with one line per player per game and the date at the start, so they can track workload over the season. Append mode is the right tool because each game adds a new entry to the end of the file without erasing the earlier ones, while write mode would wipe out the whole season’s history every time the script ran. Having that full record in order would let them spot trends, like a player’s minutes climbing over several games, and check their load management decisions later.


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
