def birthday(day,month,year):
	l = []
	l.append(day)
	l.append(month)
	l.append(year)
	
	sum = 0
	product = 1
	
	for item in l:
		print (item)
		sum += item
		product *= item
	print (sum)
	print (product)
	
rhyme = ['Mary','had','a','little','lamb','whose','fleece','was','white','as','snow']
def wlCount(L):
	length = len(L)
	wlength = 0
	
	for item in L:
		wlength += len(item)
	
	print ('There are {:d} words and {:d} letters in the rhyme'.format(length,wlength))
	print ('There are %i words and %i letters in the rhyme' % (length,wlength))
	
def fileCount():
	filename = input("Pleas type the name of the file: ")+".txt"
	lines = open(filename,'r').readlines()
	print (lines)
	sum = 0
	count = len(lines)
	for item in lines:
		if (lines.index(item)!=(count-1)):
			#print ("adding %i letters" %(len(item)) )
			sum += (len(item)-1)
		else:
			sum += len(item)

foods = ['ham','toast','spam','bacon','spinach']
def before_and_after(L,before,after):
	newList = []
	for item in L:
		newList.append(before + item + after)
	
	for item in newList:
		print(item)
	
