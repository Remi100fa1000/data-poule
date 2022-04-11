# This file contains the main file

#############
# LIBRARIES #
#############

import sys
import os
import matplotlib.pyplot as plt
import numpy as np

from datetime import datetime, timedelta # managing dates

# For importing my own files
mydir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(mydir))

#Import my own files
import library.Mycsv_func as Mycsv_func
import library.Array_func as Array_func
import library.Mygraph_func as Mygraph_func


##############
# PARAMETERS #
##############

#Path to the data file
Mypath 				= './Data.csv';

########
# CODE #
########

Mydata 				= Mycsv_func.CSV_open_file(Mypath)

# Extracting the list of dates
Mydata 				= Array_func.string_to_date(Mydata)

###################################################
# FIRST GRAPH: distribution of the weight of eggs #
###################################################

# We first get the column that contains the weight of eggs
Eggs_weight 				= Array_func.get_colum(Mydata,3)

# We transform this list of strings into a list of integers
Eggs_weight		= Array_func.list_of_string_to_list_of_int(Eggs_weight)

# Computing the average
Mean_weight 		= round(sum(Eggs_weight)/len(Eggs_weight),2)

# We want one bin per value
plt.figure(facecolor='grey') # defining background color
plt.subplots_adjust(top=0.85) # adjusting top position
plt.hist(Eggs_weight, bins =(max(Eggs_weight)-min(Eggs_weight)), range = (min(Eggs_weight)-0.5, max(Eggs_weight)-0.5),density=True, color="darkorange", ec='white')
plt.title(label="Distribution du poids des oeufs ramassés"+"\n poids moyen : "+str(Mean_weight)+ "g \n Dernière collecte le "+Mydata[len(Mydata)-1][0].strftime("%d/%m/%Y"),color='w')

plt.xticks(range(min(Eggs_weight), max(Eggs_weight)), fontsize=8)
plt.xlabel("Poids de l'oeuf (g)")

# Changing the background properties of the graph
Mygraph_func.make_better_graph()

# Saving the graph
plt.savefig('./results/dist_oeufs.png')  

###################################
# Getting the general information #
###################################
#These informations are:
#		* The duration of the study
#		* The total number of eggs

# Duration of the study

# First day
Firstdayofstudy 					= Mydata[1][0] - timedelta(days=int(Mydata[1][1])-1) # We get the first date in the array and remove the number of day since the last collect

# Last day 
Lastdayofstudy						= Mydata[len(Mydata)-1][0]

# Duration
Mydelta 							= Lastdayofstudy- Firstdayofstudy

Total_duration 						= Mydelta.days
print("Durée de l'étude :", Total_duration)

# Total number of eggs
Nb_Eggs_column 						= Array_func.get_colum(Mydata,2) # getting the column of eggs
Nb_Eggs_column							= Array_func.int_list_to_string_list(Nb_Eggs_column)
Nb_Eggs							= sum(Nb_Eggs_column[1:len(Nb_Eggs_column)-1])

print("Nombre d'oeufs :", Nb_Eggs)

# The average number of eggs per days and per chicken

# Reorganizing the array
# We make a new array which contains the list of eggs day per day
Array_per_day 						= Array_func.to_daily_stats(Mydata)

# ploting some graphs based on this new array
#############################################

# getting the columns
Daily_weight 				= Array_func.get_colum(Array_per_day,1)
Daily_nb_eggs 				= Array_func.get_colum(Array_per_day,2)
Daily_nb_hen				= Array_func.get_colum(Array_per_day,3)

# Going to numpy arrays
Daily_weight				= np.array(Daily_weight)
Daily_nb_eggs				= np.array(Daily_nb_eggs)
Daily_nb_hen				= np.array(Daily_nb_hen)

# Number of eggs per hen
Daily_egg_per_hen		 	= Daily_nb_eggs/Daily_nb_hen

# saving the result
plt.figure(facecolor='grey') # defining background color
plt.plot(Daily_egg_per_hen,color="darkorange")
plt.title(label="Nombre d'oeufs par jour et par poule",color='w')
plt.xlabel("Jours depuis le début de l'étude",color='w',fontsize=12)
plt.ylabel("Nombre d'oeufs par poule",color='w',fontsize=12)
plt.xlim(0,Total_duration-1)
# Making a better figure
Mygraph_func.make_better_graph()

plt.savefig('./results/Eggs_per_hen.png') 

# We now show the number of eggs and compare it with the maximum number of eggs (Number of hen)

# saving the result
plt.figure(facecolor='grey') # defining background color
plt.plot(Daily_nb_hen,color="g", label="Maximum") # Maximum number of eggs
plt.plot(Daily_nb_eggs,color="darkorange",label="Nombre d'oeufs")
plt.title(label="Nombre d'oeufs",color='w',fontsize=16)
plt.xlabel("Jours depuis le début de l'étude",color='w',fontsize=12)
plt.ylabel("Nombre d'oeufs",color='w',fontsize=12)
plt.xlim(0,Total_duration-1)
plt.legend()
# Making a better figure
Mygraph_func.make_better_graph()

plt.savefig('./results/Eggs_per_day.png') 

# We now show the evolution of the average weight of the eggs

Weight_of_eggs					= Daily_weight/Daily_nb_eggs

# saving the result
plt.figure(facecolor='grey') # defining background color
plt.plot(Weight_of_eggs,color="darkorange")
plt.title(label="Poids moyen des oeufs",color='w',fontsize=16)
plt.xlabel("Jours depuis le début de l'étude",color='w',fontsize=12)
plt.ylabel("Poids des oeufs",color='w',fontsize=12)
plt.xlim(0,Total_duration-1)

# Making a better figure
Mygraph_func.make_better_graph()

plt.savefig('./results/Average_daily_weight.png')

# We add an average filter so as to have better results

# We make the same graphs with a 7 days filtering

# Number of eggs per day and per hen
plt.figure(facecolor='grey') # defining background color
plt.plot(Array_func.Average_filter(Daily_egg_per_hen,7),color="darkorange")
plt.title(label="Nombre d'oeufs par jour et par poule (filtré)",color='w')
plt.xlabel("Jours depuis le début de l'étude",color='w',fontsize=12)
plt.ylabel("Nombre d'oeufs par poule",color='w',fontsize=12)
plt.xlim(0,Total_duration-1)
# Making a better figure
Mygraph_func.make_better_graph()

plt.savefig('./results/Eggs_per_hen_filtered.png') 

# We now show the number of eggs and compare it with the maximum number of eggs (Number of hen)

# saving the result
plt.figure(facecolor='grey') # defining background color
plt.plot(Daily_nb_hen,color="g", label="Maximum") # Maximum number of eggs
plt.plot(Array_func.Average_filter(Daily_nb_eggs,7),color="darkorange",label="Nombre d'oeufs")
plt.title(label="Nombre d'oeufs (filtré)",color='w',fontsize=16)
plt.xlabel("Jours depuis le début de l'étude",color='w',fontsize=12)
plt.ylabel("Nombre d'oeufs",color='w',fontsize=12)
plt.xlim(0,Total_duration-1)
plt.legend()
# Making a better figure
Mygraph_func.make_better_graph()

plt.savefig('./results/Eggs_per_day_filtered.png') 

# saving the result
plt.figure(facecolor='grey') # defining background color
plt.plot(Array_func.Average_filter(Weight_of_eggs,7),color="darkorange")
plt.title(label="Poids moyen des oeufs (filtré)",color='w',fontsize=16)
plt.xlabel("Jours depuis le début de l'étude",color='w',fontsize=12)
plt.ylabel("Poids des oeufs",color='w',fontsize=12)
plt.xlim(0,Total_duration-1)

# Making a better figure
Mygraph_func.make_better_graph()

plt.savefig('./results/Average_daily_weight_filtered.png')
