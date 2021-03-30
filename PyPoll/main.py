# PyPoll analyze votes

# import modules 
import os
import csv
import collections

input_file = os.path.join("Resources", "election_data.csv")

num_votes = 0
candidatelist = collections.defaultdict(list)

with open(input_file) as csvfile:
    input_reader = csv.DictReader(csvfile)

    for row in input_reader:
        # calculate the total number of votes
        num_votes += 1

        if row["Candidate"] not in candidatelist["Name"]:
            candidatelist["Name"].append(row["Candidate"]) 
            candidatelist[row["Candidate"]] = 1 
        else:
            candidatelist[row["Candidate"]] += 1 

    print("\n")
    print("Election Results")
    print("--------------------")
    print(f"Total Votes: {num_votes}")
    print("--------------------")
    # To print all keys and values separated by commas
    print('\n'.join(str(key) + ': ' + str(value) for key, value in candidatelist.items()))
    print("--------------------")
    print(f"Winner: {str(candidatelist[1])}")
    print("--------------------")

#output_file = os.path.join("Analysis", "analysis.txt")
#with open(output_file, 'w') as txtfile:
    #txtfile.write("\n")
    #txtfile.write("Election Results")
    #txtfile.write("--------------------")
    #txtfile.write(f"Total Votes: {num_votes}")
    #txtfile.write("--------------------")
    #txtfile.close()