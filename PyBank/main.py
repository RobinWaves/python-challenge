# PyBank analyze financial records

# import modules 
import os
import csv
from datetime import datetime

def calc_age_months(from_date, to_date):
    from_date = datetime.strptime(from_date, "%m-%Y")
    to_date = datetime.strptime(to_date, "%m-%Y")

    age_in_months = (to_date.tm_year - from_date.tm_year)*12 + (to_date.tm_mon - from_date.tm_mon)

    if to_date.tm_mday < from_date.tm_mday:
        return age_in_months -1
    else:
        return age_in_months

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    CSVreader = csv.reader(csvfile, delimiter = ',')
    
    # Read the header row first
    csv_header = next(CSVreader)
    print(f"CSV Header: {csv_header}")
    dates = []
    PL = []

    for row in CSVreader:
        dates.append(row[0])
        PL.append(row[1])
    print(f"First {dates[0]}, Last {dates[-1]} ")
    print(f"First {PL[0]}, Last {PL[-1]} ")
        
