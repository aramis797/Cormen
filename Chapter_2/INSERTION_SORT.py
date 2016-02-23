#INSERTION SORT implementation

def Insertion(A):
	for i in range(1,len(A)):
		key=A[i]
		j=i-1
		while(j >= 0 and A[j]>A[j+1]):
			temp=A[j]
			A[j]=A[j+1]
			A[j+1]=temp
			j-=1
		A[j+1]=key
if __name__ == '__main__':
	A=[5,4,3,2,1]
	print A
	Insertion(A)
	print A