def Fun1(n):
	return 100*n*n
def Fun2(n):
	return pow(2,n)
n=1
while(True):
	f1 = Fun1(n)
	f2 = Fun2(n)
	if(f1 > f2):
		print f1,f2
		n+=1
	else:
		print f1,f2,n
		break