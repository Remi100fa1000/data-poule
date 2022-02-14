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
		
		
	
