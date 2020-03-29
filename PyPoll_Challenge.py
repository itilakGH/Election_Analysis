import csv
import os



# Assign a variable to the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Creating a filename variable to a path (direct / indirect) to the file
file_to_save = os.path.join("Performing_Analysis","election_analysis.txt")

# Creating totals for the candidates and the counties and setting to zero
total_votes = 0                 #for the candidates
total_votes_counties = 0        #for the counties


# Creating two empty lists - candidates options and counties options
candidate_options = []
counties_options = []

# Declaring two empty dictionaries - for the candidates and for the counties
candidate_votes = {}
county_votes = {}

# Creating an empty srting for the largest turnout and setting counting to 0
largest_turnout = ""
largest_turnout_count = 0
largest_turnout_percentage = 0

# Creating the winner tracking and setting to 0
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election result and read the file
with open(file_to_load) as election_data:

    # Reading the file with the csv reader
    file_reader = csv.reader(election_data)

    # Removing the header that in our analysis we start counting from the second row
    headers = next(file_reader)
    #print(headers) - commenting this line because we confirmed that the table has a header and now we do not need to print it, but still want to keep in case if another file will be read

    # Counting totals, the voters turnout for each county and the number of votes for each candidate
    for row in file_reader:
        total_votes_counties = total_votes_counties +1
        total_votes = total_votes + 1
        
        candidate_name = row[2]                                         # reading the candidates in each row
        county_name = row[1]                                            # reading the counties in each row

        if county_name not in counties_options:
        
            counties_options.append(county_name)                        # adding counties to the list of options
            county_votes[county_name] = 0                               # counting begins from 0
        
        county_votes[county_name] = county_votes[county_name] + 1       # adding votes one by one to the county's count
        
        
        if candidate_name not in candidate_options:
        
            candidate_options.append(candidate_name)                    # adding candidates to the list of options
            candidate_votes[candidate_name] = 0                         # counting begins from 0

        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1   # adding votes one by one to the candidate's count

# Using the "open()" function with the "w" mode which allows to write data to the file
with open(file_to_save, "w") as txt_file:

    # Writing voters turnouts in counties in the text file.
    election_results_turnout = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total votes: {total_votes_counties:,}\n"
        f"-------------------------\n"
        f"\nCounty Votes:\n")        
    print(election_results_turnout, end="")
    txt_file.write(election_results_turnout)

             
    # 1) looking for turnouts for each county
    for counties,voters in county_votes.items():

        percentage_turnouts = voters / total_votes_counties*100
        voters = county_votes[counties]

        # creating a variable for the voters turnouts to write it to the text file (and printing in the terminal)
        turnouts_results = (
            f"{counties}: {percentage_turnouts:.1f}% ({voters:,})\n")
        print(turnouts_results)
        txt_file.write(turnouts_results)


        # Determine the county with the largest voters turnouts:

        # 1. Determine if the number of voters is greater than the turnouts count.
        if (voters > largest_turnout_count) and (percentage_turnouts > largest_turnout_percentage):
            # 2. If true then set turnout count
            largest_turnout_count = voters
            largest_turnout_percentage = percentage_turnouts
            # 3. Set the largest turnout equal to the county's name.
            largest_turnout = counties

    turnouts_summary = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {largest_turnout}\n"
        f"-------------------------\n")
    print(turnouts_summary)
    txt_file.write(turnouts_summary)


    # 2) looking for the candidates results
    for candidate,value in candidate_votes.items():

        percentage = value/total_votes*100
        votes = candidate_votes[candidate]
        
        # creating a variable for the candidates results to write it to the text file (and printing in the terminal)
        candidate_results = (
            f"{candidate}: {percentage:.1f}% ({value:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
                

        # Determine winning vote count and candidate:

        # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (percentage > winning_percentage):
            # 2. If true then set winning count
            winning_count = votes
            winning_percentage = percentage
            # 3. Set the winning candidate equal to the candidate's name.
            winning_candidate = candidate

    winning_candidate_summary = (
        f"\n-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
