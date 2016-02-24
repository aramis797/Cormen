from math import log
n=2
def INSERTION(n):
	return 8*n*n
def MERGE(n):
	return 64*n*log(n,2)
while(True):
	INS = INSERTION(n)
	MER = MERGE(n)
	if(INS < MER):
		print INS,MER
		n+=1
	else:
		print INS,MER,n
		break
