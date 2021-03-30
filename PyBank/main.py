# PyBank analyze financial records
# import modules 
import os
import csv

input_file = os.path.join("Resources", "budget_data.csv")

sum_months = 0
sum_revenue = 0

with open(input_file) as csvfile:
    input_reader = csv.DictReader(csvfile)

    for row in input_reader:
        sum_months = sum_months + 1
        sum_revenue = sum_revenue + int(row["Profit/Losses"])
    
    print(sum_months)
    
    