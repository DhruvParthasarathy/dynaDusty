# In this problem we are given coins of certain denominations, say 19 cents, 12 cents, 1 cent and 5 cents. 

# What is the minimum number of coins of the given denominations that you can use to get to the target

# For example if we need to make 16cents from [19,12,5,1] cent coins,
# We see that the smallest number of coins that can be used are 4.  
# (3)*5cents + (1)*1cent coins

# Here we see that if we go with the highest value coins first, we might either end up overshooting the target value or end up using higher number of coins, 

# The brute force would be to try all possible combinations but that would be to many iterations and a waste of computation resources

# If we look at the graph of various choices we see that we can encounter a given choice at different times as the program recurses through the tree - hence we use the memoization technique here

# The recursive relation is 
# f(denoAvail, targetVal) = Min( f(denAvail, target-denValue) + 1, f(denAvail-1, targetVal) )

import math
def minCoins ( denominationsArray, targetValue ) : 
	
	cache = {} # to save results
	
	#we define the function inside the minCoins function 
	# so that we have access to denominations array and the cache
	def subProblem (denominationIndex, valueRemaining):
		# so what does this function do
		# at any given situation it sees if we can reach the target value
		# either by selecting the given denomination coin or not


		# before we proceed to calculate check if we have any value in cache
		if((denominationIndex, valueRemaining) in cache) : return cache[(denominationIndex, valueRemaining)]
		
		# we don't have this value in cache, okay, let's proceed with next steps
		# If we chose to use the coin ? Check how the current denomination value compares to the target
		val = denominationsArray[denominationIndex]
		
		if(val == valueRemaining) : count_take = 1
		elif (val > valueRemaining) : count_take = math.inf # here we take math.inf so that it will be ignored in the REC Rel
		else : 
			count_take = subProblem(denominationIndex, valueRemaining-val) + 1

		
		# if we chose not to pick this coin
		# check if we can even leave this coin
		if(denominationIndex==0) : 
			# only this coin is avalable
			# we can never reach the target value if we take this coin, hence we have to not go with this choice
			count_leave = math.inf # we take inf so that we will have to keep repeating this step for ever and also this will be omitted in the RR
		
		else : 
			count_leave = subProblem(denominationIndex -1, valueRemaining) 
			# number of coins reduces by one, but value remaining remains the same

		
		optimal = min(count_take, count_leave)
		cache[(denominationIndex, valueRemaining)]  = optimal

		return optimal

	
	return subProblem(len(denominationsArray)-1, targetValue)


	
	
