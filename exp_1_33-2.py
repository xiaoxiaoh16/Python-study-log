numbers = []

def while_function(m,n):
	i = 0
	while(i<m):
		print "At the top i is %d"% i
		numbers.append(i)
		print "The numbers: ", numbers

		i += n
		print "Number now is: ", numbers
		print "At the bottom i is %d" % i
	return numbers


for num in while_function(6,1):
	print num
	



