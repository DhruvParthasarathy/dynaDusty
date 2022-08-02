import sys


# print the first n fibonacci numbers
# 1 1 2 3 5 8 13 ....

# Worst run time complexity : exponential
# As the value of N increases, the recursive call stack increases exponentially

def fibRec(n):
	if(n == 1 or n == 0):
		return 1
	else: return fibRec(int(n)-1) + fibRec(int(n)-2)


# Better tuntime complexity : linear run time
# Increased space usage : linearly increases as we use a cache to store data

def fib_rec_cache(n, cache):
	if n == 0 : return 1   #fib series base case
	if n == 1 : return 1	#fib series base case

	if cache is None: cache = {}	# initialize cache
	if n in cache : return cache[n]	# if we already have value in cache return it

	# value is not in cache, hence we proceed
	result = fib_rec_cache(n-1, cache) + fib_rec_cache(n-2, cache) # call the recussive loop as usual
	cache[n] = result	# save value in cache so other calls can access

	return result


# Best run time ( linear )
# Best space complexity ( constant )
# Here we solve and forget the previous values as we keep replacing the variables

def fib_n(n):

	# n can start from, 0 , means the 0th and 1st fibonacci number are 1

	fibN1 = 1	# second last value
	fibN2 = 1	# last value
	# we need to run loop only of we want to know the the 2nd fib number...
	for i in range(2, n+1):	# in range, the end value is exclusive
		
		fibN1, fibN2 = fibN2, fibN1+fibN2
		
	return fibN2
			





