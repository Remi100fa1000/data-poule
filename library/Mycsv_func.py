# This file contains all the functions which are used to open and manage my csv files

# needed libraries
import csv

# This first function imports 
def CSV_open_file(file_path):
	with open(file_path, newline='') as csvfile:
		myreader = csv.reader(csvfile, delimiter=',')
		for row in myreader:
			print(row)
