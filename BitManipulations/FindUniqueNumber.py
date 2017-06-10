def findUniqueNumber(a):
	"""Function to print unique number"""
	res = 0
	
	for i in range(len(a)):
		res = res  ^ a[i]
	
	print "Unique number is ", res, '.'

# decimal number
a=[1,2,1,3,1,2,1]

findUniqueNumber(a)
