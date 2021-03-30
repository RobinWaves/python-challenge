# PyBank analyze financial records

# import modules 
import os
import csv

input_file = os.path.join("Resources", "budget_data.csv")

sum_months = 0
sum_revenue = 0
revenue_chg = 0
prev_revenue = 0 
great_inc = ["", 0]
great_dec = ["", 9000000]
revenue_chgs = []
avg_chg = 0

with open(input_file) as csvfile:
    input_reader = csv.DictReader(csvfile)

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
    #avg_chg = sum(revenue_chgs) / len(revenue_chgs)
    avg_chg = (great_inc[1] + great_dec[1])/len(revenue_chgs)

    print("\n")
    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {sum_months}")
    print(f"Total Revenue: ${sum_revenue}")
    print(f"Average Change: ${round(avg_chg, 2)}")
    print(f"Greatest Increase in Profits: {great_inc[0]} ${great_inc[1]}")
    print(f"Greatest Decrease in Profits: {great_dec[0]} ${great_dec[1]}")