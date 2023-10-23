from audioop import avg
from email import header
import os
import csv

bank_csv = os.path.join("Resources","budget_data.csv")

with open(bank_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    total_months = 0
    total_profit= 0
    avg_change = 0
    gain_max = 0
    loss_max = 0

    header = next(csv_reader)

    for row in csv_reader:
        total_months += 1
        total_profit = total_profit + int(row[1])
        if int(row[1]) > int(gain_max):
            gain_max = row[1]
            gain_date = row[0]
        if int(row[1]) < int(loss_max):
            loss_max = row[1]
            loss_date = row[0]

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit}")
    avg_change = total_profit / total_months
    print(f"Average Change: ${avg_change}")
    print(f"Greatest Increase in Profits: {gain_date} (${gain_max})")
    print(f"Greatest Decrease in Profits: {loss_date} (${loss_max})")

bank_output = os.path.join("Analysis","analysis.txt")
with open(bank_output,'w') as f:
    f.write("Financial Analysis\n")
    f.write("----------------------------\n")
    f.write(f"Total Months: {total_months}\n")
    f.write(f"Total: ${total_profit}\n")
    f.write(f"Average Change: ${avg_change}\n")
    f.write(f"Greatest Increase in Profits: {gain_date} (${gain_max})\n")
    f.write(f"Greatest Decrease in Profits: {loss_date} (${loss_max})\n")