# This file contains all the functions necessary for the management of the array

# Necessary packages
from datetime import datetime, timedelta

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
	
# This function changes a list of str into a list of int
def int_list_to_string_list(Mylistofstring):

	Result				= [];	
	
	# We append each element 
	for i in range(0, len(Mylistofstring)):
		Result.append(int(Mylistofstring[i]))
		
	return Result

# This function changes the array of eggs collected into an array that contains statistics day per day
def to_daily_stats(Mycsv):

	# My result as an array
	Myresult 						= []
	
	# First day of the study
	Firstdayofstudy 				= Mycsv[1][0] - timedelta(days=int(Mycsv[1][1])-1) # We get the first date in the array and remove the number of day since the last collect
	
	# Duration of the study
	# Last day 
	Lastdayofstudy					= Mycsv[len(Mycsv)-1][0]

	# Duration
	Mydelta 						= Lastdayofstudy- Firstdayofstudy

	Total_duration 					= Mydelta.days+1
	# We make a list which contains all the dates
	Listofdate						= []
	
	# We fill the array which contains all the dates
	for i in range(Total_duration):
		Listofdate.append(Firstdayofstudy+timedelta(days=i))
	
	# We now get:
		# the number of eggs per day and 
		# the total weight per day
		# the number of chicken every day
	
	# When one collect is done for several day, we use the average number of eggs by dividing the number of eggs by the duration of the collect
	# We now make one list for every metric
	Total_weight_per_day		= [0]*Total_duration
	Nb_eggs_per_day		= [0]*Total_duration
	Nb_chicken_per_day		= [0]*Total_duration
	
	# We fill these lists
	for i in range(1,len(Mycsv)):

		# Finding the current date
		Current_date						= Mycsv[i][0]
		Last_index						= Current_date-Firstdayofstudy # Last index for this box
		Last_index						= Last_index.days

		# Getting all the eggs for this collect
		Eggs_weight						= Mycsv[i][3].split(',')
		Total_weight						= 0
		
		for j in range(len(Eggs_weight)):
			if(len(Eggs_weight[j].strip())>0): # We check if the box is not empty
				Total_weight						= Total_weight+int(Eggs_weight[j])
		
		# For each box in the array, we have as many boxes to fill in the new array as in the column 2
		for j in range(int(Mycsv[i][1])):
			Total_weight_per_day[Last_index-j]				= Total_weight_per_day[Last_index-j]+Total_weight/int(Mycsv[i][1])
			
		
		# filling the array which contains the number of eggs
		for j in range(int(Mycsv[i][1])):
			Nb_eggs_per_day[Last_index-j]					= Nb_eggs_per_day[Last_index-j]+int(Mycsv[i][2])/int(Mycsv[i][1])

		for j in range(int(Mycsv[i][1])):
			Nb_chicken_per_day[Last_index-j]				= int(Mycsv[i][4])
	
	# We now fill the result which is an array which contains all the lists
	for i in range(len(Listofdate)):
		Myresult.append([Listofdate[i], Total_weight_per_day[i],Nb_eggs_per_day[i], Nb_chicken_per_day[i]])
	
	return Myresult
