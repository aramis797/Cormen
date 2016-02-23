#HEAPSORT Implementation
def PARENT(i):
	return i/2
def LEFT(i):
	return 2*i
def RIGHT(i):
	return (2*i) + 1
def MAX_HEAPIFY(A,i):
	global heap_size
	l=LEFT(i)
	r=RIGHT(i)
	if(l <= heap_size and A[l]>A[i]):
		largest=l
	else:
		largest=i
	if(r <= heap_size and A[r]>A[largest]):
		largest=r
	if(largest != i):
		temp=A[i]
		A[i]=A[largest]
		A[largest]=temp
		MAX_HEAPIFY(A,largest)
def BUILD_MAX_HEAP(A):
	global heap_size
	for i in range(heap_size/2,0,-1):
		MAX_HEAPIFY(A,i)
def HEAP_SORT(A):
	BUILD_MAX_HEAP(A)
	global heap_size
	while(heap_size > 1):
		temp=A[1]
		A[1]=A[heap_size]
		A[heap_size]=temp
		heap_size-=1
		MAX_HEAPIFY(A,1)
if __name__ == '__main__':
#	A=[0,9,8,7,6,5,4,3,2,1,0]
#	A=[0,27,17,3,16,13,10,1,5,7,12,4,8,9,0]
	A=[0,1,5,9,3,4,8,7]
	heap_size=len(A)-1
	print A
#	HEAP_SORT(A)
	MAX_HEAPIFY(A,1)
	print A