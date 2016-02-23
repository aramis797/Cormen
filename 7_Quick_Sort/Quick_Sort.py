def PARTITION(A,p,r):
	X=A[r]
	i=p-1
	for j in range(p,r):
		if A[j] <= X:
			i+=1
			temp=A[i]
			A[i]=A[j]
			A[j]=temp
	temp=A[i+1]
	A[i+1]=A[r]
	A[r]=temp
	return i+1
A=[2,8,7,1,3,5,6,4]
print A
print PARTITION(A,0,len(A)-1)
print A