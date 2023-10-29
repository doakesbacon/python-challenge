import os
import csv

# Define the path to the CSV file
csvpath = os.path.join( "Resources", "election_data.csv")
#print("Current working directory:", os.getcwd())
#print(csvpath)

 # Define variables to store the vote data 
totalvotes = 0 
candidates  = {}
winnervotes = 0
winnername = ""


 # Open the CSV file using the csvpath variable
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip the header row
    header = next(csvreader)

    # Loop through each row in the CSV file
    for row in csvreader:
        # Extract who got the vote 
        Can_vote = row[2]

        #will update the votes per candidate or add a new one with a vote if not alreasy in list 
        if Can_vote in candidates:
            candidates[Can_vote] += 1
        else:
            candidates[Can_vote] = 1

        #Updates total votes
        totalvotes += 1 


# find and set the winner
for Can_vote, votes in candidates.items():
    if votes > winnervotes:
        winnername = Can_vote 
        winnervotes = votes


print("Election Results")
print("-------------------------")
print(f"Total Votes: {totalvotes}")
print("-------------------------")

for Can_vote, votes in candidates.items():
    percent = (votes / totalvotes) * 100
    print(f"{Can_vote}: {percent:.3f}% ({votes})")

print("-------------------------")
print(f"Winner: {winnername}")
print("-------------------------")

output_file = os.path.join("analysis" , "election_results.txt")
# \n is new line 
with open(output_file, "w") as output_file:
    output_file.write("Election Results\n")
    output_file.write("------------------\n")
    output_file.write(f"Total Votes: {votes}\n")
    
    for Canvote, votes in candidates.items():
        percent = (votes / totalvotes) * 100
        output_file.write(f"{Canvote}: {percent:.3f}% ({votes})\n")

    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winnername}\n")
    output_file.write("-------------------------\n")
