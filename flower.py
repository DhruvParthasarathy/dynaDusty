# in this problem we have an array of n spots, where each spot has a given value associated with it

# Planting a flower at that spot will make it grow to height i

# We cannot plant flowers next to each other

# Find the max total height that can be achieved given the array of values for each spot

# We use a recurrence relation here that f(i) = Max(Vi + f(i-2), f(i-1) )

def flower(valuesArray):
	# we have an array of values
	# recurrence relation is f(i) = MAX(vi + f(i-2), f(i-1))
	# If we draw the DAG, we will see that even for f(0), we can follow the same
	# Just that here both f(i-2) and f(i-1) will be 0
	# hence we can start with a, b = 0 , and proceed with the iteration
	# for all values in the array
	
	a = 0 # used to store value of f(i-2) 
	b = 0 # used to store value of f(i-1)
	for val in valuesArray :
		a , b = b, max(val + a, b)
	return b
		
		
