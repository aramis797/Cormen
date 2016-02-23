def LEFT(i):
    return 2*i
def RIGHT(i):
    return 2*i+1
def PARENT(i):
    return i/2
def MIN_HEAPIFY(A,i):
    global heap_size
    l=LEFT(i)
    r=RIGHT(i)
    if(l<=heap_size and A[l]<A[i]):
        smallest = l
    else:
        smallest = i
    if(r<=heap_size and A[r]<A[smallest]):
        smallest=r
    if(smallest != i):
        temp=A[i]
        A[i]=A[smallest]
        A[smallest]=temp
        MIN_HEAPIFY(A,smallest)
def BUILD_MIN_HEAP(A):
    global heap_size
    for i in range(len(A)/2,0,-1):
        MIN_HEAPIFY(A,i)
A=[0,16,4,10,14,7,9,3,2,8,1]
print A
heap_size=len(A)-1
BUILD_MIN_HEAP(A)
print A
