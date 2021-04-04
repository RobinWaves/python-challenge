# PyBank analyze financial records

# import modules 
import os
import csv

input_file = os.path.join("Resources", "budget_data.csv")
#assign variables
revenue_chg = 0
avg_chg = 0
great_inc = ["", 0]
great_dec = ["", 9000000]
revenue_chgs = []

with open(input_file) as csvfile:
    input_reader = csv.DictReader(csvfile)
    
    # reads first row and assigns previous_revenue
    first_row = next(input_reader)
    prev_revenue = int(first_row["Profit/Losses"])
    
    # initalize sum of months and sum of revenue assigned because took off first row
    sum_revenue = int(first_row["Profit/Losses"])
    sum_months = 1
    
    for row in input_reader:
        # calculate the total number of months and revenue
        sum_months += 1
        sum_revenue += int(row["Profit/Losses"])
       
        # calculate the revenue change from previous month to current month
        revenue_chg = int(row["Profit/Losses"]) - prev_revenue
        # set previous revenue for next iteration
        prev_revenue = int(row["Profit/Losses"])
        # finds greatest revenue increase and greatest revenue decrease
        if revenue_chg > great_inc[1]:
            great_inc[0] = row["Date"]
            great_inc[1] = revenue_chg
        if revenue_chg < great_dec[1]:
            great_dec[0] = row["Date"]
            great_dec[1] = revenue_chg
        # adds revenue change to list
        revenue_chgs.append(revenue_chg)
    
    # finds average of revenue changes
    avg_chg = sum(revenue_chgs) / len(revenue_chgs)
    
# print in terminal
print("\n")
print("Financial Analysis")
print("------------------")
print(f"Total Months: {sum_months}")
print(f"Total Revenue: ${sum_revenue}")
print(f"Average Change: ${round(avg_chg, 2)}")
print(f"Greatest Increase in Profits: {great_inc[0]} ${great_inc[1]}")
print(f"Greatest Decrease in Profits: {great_dec[0]} ${great_dec[1]}")

# create and print output file
output_file = os.path.join("Analysis", "analysis.txt")

with open(output_file, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("------------------\n")
    txtfile.write(f"Total Months: {sum_months}\n")
    txtfile.write(f"Total Revenue: ${sum_revenue}\n")
    txtfile.write(f"Average Change: ${round(avg_chg, 2)}\n")
    txtfile.write(f"Greatest Increase in Profits: {great_inc[0]} ${great_inc[1]}\n")
    txtfile.write(f"Greatest Decrease in Profits: {great_dec[0]} ${great_dec[1]}")
    txtfile.close()