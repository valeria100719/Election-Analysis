# the data we need to retrieve
#1. the tot number of votes cast
#2.complete list of candidates who received votes
#3.%of votes each candidate won
#4.total number of votes each candidate won
#5.the winner of election based on popular votes
# Import the datetime class from the datetime module.
# Import the datetime class from the datetime module.

# exercise
#open the election result and read the file.
#create a file variable to direct or indirect path where the file is located
#file_to_load="resources/election_results.csv"

#election_data=open(file_to_load,'r')
#to do: perform amalysis.
#close the file.
#election_data.close()
# use open() function in the mode that u want to open the file
# Open the election results and read the file
#with open(file_to_load) as election_data:

     # To do: perform analysis.
     #print(election_data)
#import csv
#import os
# Assign a variable for the file to load and the path.
#ile_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
#with open(file_to_load) as election_data:

    # Print the file object.
    #print(election_data)
# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    #txt_file.write("Hello World")
    #txt_file.write("Arapahoe")
    #txt_file.write("Denver")
    #txt_file.write("Jefferson")

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader= csv.reader(election_data)
    # Print the header row.
    headers = next(file_reader)
    print(headers)