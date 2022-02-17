# This file contains all the functions which are used to open and manage my csv files

# needed libraries
import csv

# This first function imports the data from the array in a double dimensional list
def CSV_open_file(file_path):
	
	Mylist 		= [] # We create an empty list	
	
	with open(file_path, newline='') as csvfile:
		myreader = csv.reader(csvfile, delimiter=',')
		for row in myreader:
			Mylist.append(row)
			
	return Mylist
	

