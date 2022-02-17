# This file contains the main file

#############
# LIBRARIES #
#############

import sys
import os
import matplotlib.pyplot as plt
# For importing my own files
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

#Import my own files
import library.Mycsv_func as Mycsv_func
import library.Array_func as Array_func

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
print(Eggs_weight)

plt.hist(Eggs_weight)
plt.show()

# Reorganizing the array
