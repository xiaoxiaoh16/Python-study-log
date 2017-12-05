i=0
numbers = []
while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)
	
	print "The numbers: ", numbers
	
	i=i+ 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i

for num in numbers:
	print num
