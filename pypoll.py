# the data we need to retrieve
#1. the tot number of votes cast
#2.complete list of candidates who received votes
#3.%of votes each candidate won
#4.total number of votes each candidate won
#5.the winner of election based on popular votes
# Import the datetime class from the datetime module.
# Import the datetime class from the datetime module.
file_to_load='Resources/election_results.cvs'
election_results=open(file_to_load,'r')
election_data.close()
file_to_save=os.path.join(analysis,"election_analysis.txt")
open(file_to_save,"w")
