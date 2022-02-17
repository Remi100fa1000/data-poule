# This file contains all the functions necessary for the management of the array

# Necessary packages
from datetime import datetime

# This function changes the first column (date) into a datetime format
# As a parameter we have the double dimensional list which contains 

def string_to_date(From_csv_list):
	# New double dimensional array
	Result 						= From_csv_list;
	
	# conversion to datetime format
	for i in range(1,len(From_csv_list)):
		Result[i][0] 					= datetime.strptime(From_csv_list[i][0],'%d/%m/%y')
	
	# Returning result
	return Result

# This function aims at getting one column of an array from a csv
def get_colum(Mycsv,Index_column):
	
	# empty list which contains the result
	Result 						= [];
	
	# We start at one to avoid the title of the column
	for i in range(1,len(Mycsv)):
		Result.append(Mycsv[i][Index_column])
	
	return Result

# This function changes the list of strings which contains all the weights into a list of integers
def list_of_string_to_list_of_int(Mylistofstring):
	
	# Temp variable
	Tmp					= []
	# This variable contains the result
	Result					= []

	for i in range(0,len(Mylistofstring)):
		# We use extend to add element by element
		Tmp.extend(Mylistofstring[i].split(','))
	
	# We convert the elements into int
	for i in range(0, len(Tmp)):
		if len(Tmp[i].strip())>0:
			Result.append(int(Tmp[i]))
		
	return Result
