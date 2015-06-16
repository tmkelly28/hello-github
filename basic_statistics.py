"""basic-statistics.py
Calculates the mean, standard deviation or variance of the data in a file
"""

from math import sqrt

def calculateFormulas(file):
	"""Accepts file input as a list of strings to be converted into ints.

	Returns mean, variance, and standard_deviation of the int values of the list as ints.
	"""
	count = 0
	sum = 0
	variance_sum = 0
	for _ in file:
		sum += int(_)
		count += 1
	mean = sum / count
	
	for _ in file:
		variance_sum += (int(_) - mean) ** 2
	variance = variance_sum / count
	standard_deviation = sqrt(variance)
	
	return mean, variance, standard_deviation
	
def newCalculation():
	new_calculation = raw_input("Awesome! Would you like do another calculation (y/n)? ").lower()
	if new_calculation[0] == "y":
		main()
	elif new_calculation[0] == "n":
		print "Okay! See you later!"
	
def main():
	print "Let's do some statistics formulas!"
	print "First off, what file are we getting our data from?"
	print "This should be a .txt file, with each value on a separate line."
	
	filename = raw_input("Filename: ")
	infile = open(filename, 'r')
	file = (infile.read()).split("\n")
	
	mean, variance, standard_deviation = calculateFormulas(file)
	
	print "The mean of this dataset is: " + str(mean)
	print "The variance of this dataset is " + str(variance)
	print "The standard deviation of this dataset is " + str(standard_deviation)
	
	infile.close()
	newCalculation()
	
if __name__ == "__main__":
	main()