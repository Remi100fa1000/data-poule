# This package contains a set of functions which are used to make my graphs more beautiful

# Necessary packages
import matplotlib.pyplot as plt

# This function changes the characteristics of the graph that has recently been created
def make_better_graph():
	ax 				= plt.gca() # getting the graph to change its properties
	
	# chosen properties to give the graph a better look
	ax.yaxis.grid()
	ax.set_axisbelow(True)
	ax.set_facecolor('grey')
	ax.spines['bottom'].set_color('white')
	ax.spines['top'].set_color('white')
	ax.spines['right'].set_color('white')
	ax.spines['left'].set_color('white')
	ax.xaxis.label.set_color('white')
	ax.tick_params(colors='white')




