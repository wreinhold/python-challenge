import os
import csv

# Set up path to read csv 
bank_csv = os.path.join("Resources","budget_data.csv")

# Opened & Read file into reader
with open(bank_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Set up variables for future use
    total_months = 0
    total_profit= 0
    avg_change = 0
    gain_max = 0
    loss_max = 0

    # Took in Header data
    header = next(csv_reader)

    # Created a loop to count the total months (rows) in the data set & calculated the total profit in the set
    for row in csv_reader:
        total_months += 1
        total_profit = total_profit + int(row[1])
        
        # Searched for the max gain by comparing the entry to the current highest
        if int(row[1]) > int(gain_max):
            gain_max = row[1]
            gain_date = row[0]
        # performed the inverse of above for the max loss
        if int(row[1]) < int(loss_max):
            loss_max = row[1]
            loss_date = row[0]

    # Printed out the results of the analysis to the user in the terminal
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit}")
    # Calculated the average change for each month
    avg_change = total_profit / total_months
    print(f"Average Change: ${avg_change}")
    print(f"Greatest Increase in Profits: {gain_date} (${gain_max})")
    print(f"Greatest Decrease in Profits: {loss_date} (${loss_max})")

# Output the same results as above to an analysis text file for the user
bank_output = os.path.join("Analysis","analysis.txt")
with open(bank_output,'w') as f:
    f.write("Financial Analysis\n")
    f.write("----------------------------\n")
    f.write(f"Total Months: {total_months}\n")
    f.write(f"Total: ${total_profit}\n")
    f.write(f"Average Change: ${avg_change}\n")
    f.write(f"Greatest Increase in Profits: {gain_date} (${gain_max})\n")
    f.write(f"Greatest Decrease in Profits: {loss_date} (${loss_max})\n")