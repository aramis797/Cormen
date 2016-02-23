# Merge Sort implementaion without using sentinels
def Merge(A,p,q,r):
	n1=q-p+1
	n2=r-q
	L=[];R=[]
	for i in range(n1):
		L.append(A[p+i])
	for j in range(1,n2+1):
		R.append(A[q+j])
	for k in range(p,r+1):
		if(len(L)>0 and len(R)>0):
			if(L[0]<=R[0]):
				A[k]=L[0]
				del L[0]
			else:
				A[k]=R[0]
				del R[0]
		else:
			if(len(L)==0):
				A[k:r+1]=R
				break
			else:
				A[k:r+1]=L
				break
def Merge_Sort(A,p,r):
	if(p<r):
		q=(p+r)/2
		Merge_Sort(A,p,q)
		Merge_Sort(A,q+1,r)
		Merge(A,p,q,r)
if __name__ == '__main__':
	A=[9,8,7,6,5,4,3,2,1]
	print A
	Merge_Sort(A,0,len(A)-1)
	print A