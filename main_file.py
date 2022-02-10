# This file contains the main file

#############
# LIBRARIES #
#############

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
print(SCRIPT_DIR)
sys.path.append(os.path.dirname(SCRIPT_DIR))

from Mycsv_func.py import CSV_open_file

##############
# PARAMETERS #
##############

#Path to the data file
Mypath 				= './Data.csv';

########
# CODE #
########

CSV_open_file(Mypath)
