# The data we need to retrieve

# 1. The total number of votes cast

# 2. A complete list of candidates who received votes

# 3. The percentage of votes each candidate wone

# 4. The total number of vootes each candidate won

# 5. The winner of the election based on popular vote

# Import Dependencies
import csv
import os

# Assign variable to save file to a path
file_to_save = os.path.join("Module_3", "election-analysis", "Analysis", "election_analysis.txt")

# Assign variable to load file from path
file_to_load = os.path.join("Module_3", "election-analysis", "Resources", "election_results.csv")

# Open election results and read file
with open(file_to_load, "r") as election_data:


    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Print the header row
    headers = next(file_reader)
    print(headers)
    

