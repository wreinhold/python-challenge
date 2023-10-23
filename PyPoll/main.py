import os
import csv

poll_csv = os.path.join("Resources","election_data.csv")

with open(poll_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    total_votes = 0
    candidates= {}
    highest_votes = 0
    winner = ""

    header = next(csv_reader)

    for row in csv_reader:
        total_votes += 1
        if row[2] not in candidates:
            candidates[row[2]] = 1
        else:
            candidates[row[2]] += 1
          
    print("Election Analysis")
    print("----------------------------")
    print(f"Total Votes: {total_votes}")
    for candidate in candidates:
        print(f"{candidate}: {round(candidates[candidate]/int(total_votes) * 100, 3)}% ({candidates[candidate]})")
        if int(candidates[candidate]) > int(highest_votes):
            winner = candidate
            highest_votes = candidates[candidate]
    print("----------------------------")
    print(f"Winner: {winner}")
    print("----------------------------")

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