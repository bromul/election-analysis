# Import Dependencies
import csv
import os

# Assign variable to save file to a path
file_to_save = os.path.join("Module_3", "election-analysis", "Analysis", "election_analysis.txt")

# Assign variable to load file from path
file_to_load = os.path.join("Module_3", "election-analysis", "Resources", "election_results.csv")

# Initialize a total vote counter
total_votes = 0

# Candidate Options
candidate_options = []

# Declare empty dictionary
candidate_votes = {}

#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open election results and read file
with open(file_to_load, "r") as election_data:


    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)
    
    # Add to total vote count
    for row in file_reader:
        total_votes += 1

        # Print candidate name from each row
        candidate_name = row[2]

        # Add the candidate name to the candidate list
        if candidate_name not in candidate_options:
            
            # Add nome to list
            candidate_options.append(candidate_name)
            
            # Begin tracking candidate vote count
            candidate_votes[candidate_name] = 0   

        # Add a vote to candidate's count
        candidate_votes[candidate_name] += 1 


# Calculate vote percentage
for candidate_name in candidate_options:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100

    # Determine winning vote count and candidate
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #Set winning_count = votes and winning_percentage = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        # Declare winner
        winning_candidate = candidate_name

    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")


winning_candidate_summary = (
    f"--------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"--------------------------\n")
print(winning_candidate_summary)



