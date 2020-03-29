import csv
import os



# Assign a variable to the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Creating a filename variable to a path (direct / indirect) to the file
file_to_save = os.path.join("Performing_Analysis","election_analysis.txt")

# Setting total to zero
total_votes = 0


# Listing candidates options list
candidate_options = []

# declaring an empty dictionary
candidate_votes = {}

# setting the winner tracking
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the elevtion result and read the file
with open(file_to_load) as election_data:

    #To do: perform the analysis
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    #print(headers)

    for row in file_reader:
        total_votes = total_votes + 1
        # reading the candidates in each row
        candidate_name = row[2]
        
        
        if candidate_name not in candidate_options:
        # adding candidates to the list of options
            candidate_options.append(candidate_name)

            # counting begins from 0
            candidate_votes[candidate_name] = 0

        # adding votes one by one to the candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

#Using the "open()" function with the "w" mode which allows to write data to the file
with open(file_to_save, "w") as txt_file:

    # Writing election results in the text file.
    election_res = (
        f"\nElection Results\n"
        f"--------------------------\n"
        f"Total votes: {total_votes:,}\n"
        f"------------------------------\n")
    print(election_res, end="")
    txt_file.write(election_res)
            

    for candidate,value in candidate_votes.items():
            
        percentage = value/total_votes*100
        votes = candidate_votes[candidate]
        # printing the result
        #print(f"{candidate}: {percentage:.2f}% ({value:,})\n") - commenting as guided

        # creating a variable for the candidates results to write it to the text file (instead of printing in the terminal)
        candidate_results = (
            f"{candidate}: {percentage:.2f}% ({value:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
        

            

        # Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (percentage > winning_percentage):
            # 2. If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = percentage
            # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.2f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)





    



# The data we need to retrieve:
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote