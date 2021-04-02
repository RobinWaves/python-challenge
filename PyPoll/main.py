# PyPoll analyze votes

# import modules 
import os
import csv

input_file = os.path.join("Resources", "election_data.csv")

num_votes = 0
candidatelist = []
candidatevotes = {}

with open(input_file) as csvfile:
    # Headers: Voter ID,County,Candidate
    input_reader = csv.DictReader(csvfile)

    for row in input_reader:
        # calculate the total number of votes
        num_votes += 1
        # https://www.geeksforgeeks.org/python-count-occurrences-of-each-word-in-given-text-file-using-dictionary/
        if row["Candidate"] not in candidatelist:
            candidatelist.append(row["Candidate"])
            candidatevotes[row["Candidate"]] = 1
        else:
            candidatevotes[row["Candidate"]] = candidatevotes[row["Candidate"]] + 1
        
print("\n")
print("Election Results")
print("--------------------")
print(f"Total Votes: {num_votes}")
print("--------------------")
for candidate in candidatevotes:
    print(f"{candidate}: {(candidatevotes[candidate]/num_votes) * 100 :.3f}% {candidatevotes[candidate]}")

#output_file = os.path.join("Analysis", "analysis.txt")
#with open(output_file, 'w') as txtfile:
    #txtfile.write("\n")
    #txtfile.write("Election Results")
    #txtfile.write("--------------------")
    #txtfile.write(f"Total Votes: {num_votes}")
    #txtfile.write("--------------------")
    #txtfile.close()