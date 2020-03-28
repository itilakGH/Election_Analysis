import csv
import os


# Assign a variable to the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Creating a filename variable to a path (direct / indirect) to the file
file_to_save = os.path.join("Performing_Analysis","election_analysis.txt")

# Open the elevtion result and read the file
with open(file_to_load) as election_data:

    #To do: perform the analysis
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    print(headers)

    for row in file_reader:
       print(row)



#Using the "open()" function with the "w" mode which allows to write data to the file
#with open(file_to_save, "w") as txt_file:

    # Writing some text in the file.
    #txt_file.write("Counties in the Election\n____________________\n")
    #txt_file.write("Arapahoe\nDenver\nJefferson")



# The data we need to retrieve:
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote