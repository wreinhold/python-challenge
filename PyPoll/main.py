import os
import csv

# Set up path to read csv 
poll_csv = os.path.join("Resources","election_data.csv")

# Opened & Read file into reader
with open(poll_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Set up variables for future use
    total_votes = 0
    candidates= {}
    highest_votes = 0
    winner = ""

    # Took in Header data
    header = next(csv_reader)

    # Counted total number of votes using for loop and filled the candidates dictionary based on if the candidate was already in
    # the dictionary. Added plus one for every occurance of the candidates name
    for row in csv_reader:
        total_votes += 1
        if row[2] not in candidates:
            candidates[row[2]] = 1
        else:
            candidates[row[2]] += 1
          
    # Printed out the results of the election to the terminal
    print("Election Analysis")
    print("----------------------------")
    print(f"Total Votes: {total_votes}")
    # Created a loop to list the candidate, calculate the vote percentage, and determine the winner
    for candidate in candidates:
        print(f"{candidate}: {round(candidates[candidate]/int(total_votes) * 100, 3)}% ({candidates[candidate]})")
        if int(candidates[candidate]) > int(highest_votes):
            winner = candidate
            highest_votes = candidates[candidate]
    print("----------------------------")
    print(f"Winner: {winner}")
    print("----------------------------")

# Output the same results as above to an analysis text file
poll_output = os.path.join("Analysis","analysis.txt")
with open(poll_output,'w') as f:
    f.write("Election Analysis\n")
    f.write("----------------------------\n")
    f.write(f"Total Votes: {total_votes}\n")
    for candidate in candidates:
        f.write(f"{candidate}: {round(candidates[candidate]/int(total_votes) * 100, 3)}% ({candidates[candidate]})\n")
    f.write("----------------------------\n")
    f.write(f"Winner: {winner}\n")
    f.write("----------------------------\n")