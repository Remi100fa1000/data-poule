# This file contains the main file

#############
# LIBRARIES #
#############

import sys
import os

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
Array_func.string_to_date(Mydata)

# Reorganizing the array
