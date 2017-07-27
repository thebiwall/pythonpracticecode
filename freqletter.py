def fl(l):
	l = l.lower()
	a = ''.join(x for x in l if x.isalpha())
	a = list(a)
	i = 0
	x = 0
	zfreq = 0
	z = ''
	while i < len(a):
		if i == 0:
			zfreq = a.count(a[i])
			print('The first count is:', zfreq)
			z = i
			print(z)
		else:
		    x = a.count(a[i])
		    print ('This is x:',x)
		    print ('This is i:',i)
		    print (a.count(a[i]))
		    if x > zfreq:
		    	z = i
		    	zfreq  = x
		    if x == zfreq and i > z:
		    	z = i
		i = i + 1
	return a[z]


l = "Hello"
fl(l)