# PyPoll analyze votes

# import modules 
import os
import csv

input_file = os.path.join("Resources", "election_data.csv")

num_votes = 0
candidatelist = []
candidatevotes = {}

with open(input_file) as csvfile:
    # read file into a dictionary
    input_reader = csv.DictReader(csvfile)
    # Keys: Voter ID, County, Candidate
    for row in input_reader:
        # calculate the total number of votes
        num_votes += 1
        # https://www.geeksforgeeks.org/python-count-occurrences-of-each-word-in-given-text-file-using-dictionary/
        if row["Candidate"] not in candidatelist:
            candidatelist.append(row["Candidate"])
            candidatevotes[row["Candidate"]] = 1
        else:
            candidatevotes[row["Candidate"]] = candidatevotes[row["Candidate"]] + 1
        
print("\nElection Results")
print("--------------------")
print(f"Total Votes: {num_votes}")
print("--------------------")
for candidate in candidatevotes:
    print(f"{candidate}: {(candidatevotes[candidate]/num_votes) * 100 :.3f}% {candidatevotes[candidate]}")
print("--------------------")
print(f"Winner: {candidatelist[0]}")
print("--------------------")

output_file = os.path.join("Analysis", "analysis.txt")

with open(output_file, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("--------------------\n")
    txtfile.write(f"Total Votes: {num_votes}\n")
    txtfile.write("--------------------\n")
    for candidate in candidatevotes:
        txtfile.write(f"{candidate}: {(candidatevotes[candidate]/num_votes) * 100 :.3f}% {candidatevotes[candidate]}\n")
    txtfile.write("--------------------\n")
    txtfile.write(f"Winner: {candidatelist[0]}\n")
    txtfile.write("--------------------")
    txtfile.close()