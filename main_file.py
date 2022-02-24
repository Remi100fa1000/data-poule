# This file contains the main file

#############
# LIBRARIES #
#############

import sys
import os
import matplotlib.pyplot as plt
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

plt.hist(Eggs_weight, bins =(max(Eggs_weight)-min(Eggs_weight)), range = (min(Eggs_weight)-0.5, max(Eggs_weight)-0.5),density=True, color="darkorange", ec='white')
plt.title(label="Distribution du poids des oeufs ramassés"+"\n poids moyen : "+str(Mean_weight)+ "g \n Dernière collecte le "+Mydata[len(Mydata)-1][0].strftime("%d/%m/%Y"),color='w')

plt.xticks(range(min(Eggs_weight), max(Eggs_weight)))
plt.xlabel("Poids de l'oeuf (g)")

# Changing the background properties of the graph
Mygraph_func.make_better_graph()

# Saving the graph
plt.savefig('./results/dist_oeufs.pdf')  




# Reorganizing the array
