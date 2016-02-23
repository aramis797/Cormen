def PARENT(i):
	return i/2
def LEFT(i):
	return 2*i
def RIGHT(i):
	return (2*i)+1
def MAX_HEAPIFY(A,i):
	global heap_size
	l=LEFT(i)
	r=RIGHT(i)
	if(l<=heap_size and A[l]>A[i]):
		largest=l
	else:
		largest=i
	if(r<=heap_size and A[r]>A[largest]):
		largest=r
	if(largest != i):
		temp=A[i]
		A[i]=A[largest]
		A[largest]=temp
		MAX_HEAPIFY(A,largest)
def BUILD_MAX_HEAP(A):
	for i in range((len(A)/2),0,-1):
		MAX_HEAPIFY(A,i)
def HEAP_SORT(A):
    global heap_size
    for i in range(len(A)-1,1,-1):
        print A
        temp=A[i]
        A[i]=A[1]
        A[1]=temp
        heap_size-=1
        MAX_HEAPIFY(A,1)

A=[0,16,4,10,14,7,9,3,2,8,1]
#A=[0,27,17,3,16,13,10,1,5,7,12,4,8,9,0]
#A=[0,4,1,3,2,16,9,10,14,8,7]
print A
heap_size=len(A)-1
BUILD_MAX_HEAP(A)
HEAP_SORT(A)
print A
