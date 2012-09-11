def isNotValid(x):
	a = int(str(x)[0])
	b = int(str(x)[1])
	c = int(str(x)[2])
	d = int(str(x)[3])
	e = int(str(x)[4])
	r =[a,b,c,d,e]

	if a * b != 24:
		return False

	if b % 2 != 0:
		return False

	if d != b/2:
		return False

	if (a + c != d + e):
		return False
			
	if (a+b+c+d+e != 26):
		return False
	
	h = False
	for f in range (5):
		for x in range (f+1,5):
			if r[f] == r[x]:
				h = True
	if h:
		print "We won! -> " + str(r)
			

for f in range (99999):
	x = '%05d'%f
	isNotValid(x)