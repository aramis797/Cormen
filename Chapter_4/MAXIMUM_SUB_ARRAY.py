def FIND_MAX_CROSSING_SUBARRAY(A,low,mid,high):
	left_sum=Sum=A[mid]
	max_left=mid
	for i in range(mid-1,low-1,-1):
		Sum+=A[i]
		if(Sum > left_sum):
			left_sum = Sum
			max_left = i
	right_sum=Sum=A[mid+1]
	max_right=mid+1
	for j in range(mid+2,high+1):
		Sum+=A[j]
		if(Sum > right_sum):
			right_sum=Sum
			max_right=j
	return (max_left,max_right,left_sum+right_sum)
def FIND_MAXIMUM_SUB_ARRAY(A,low,high):
	if(low == high):
		return (low,high,A[low])
	else:
		mid=(low+high)/2
		(left_low,left_high,left_sum)=FIND_MAXIMUM_SUB_ARRAY(A,low,mid)
		(right_low,right_high,right_sum)=FIND_MAXIMUM_SUB_ARRAY(A,mid+1,high)
		(cross_low,cross_high,cross_sum)=FIND_MAX_CROSSING_SUBARRAY(A,low,mid,high)
		if(left_sum >=right_sum and left_sum >= cross_sum):
			return (left_low,left_high,left_sum)
		elif(right_sum >= left_sum and right_sum>=cross_sum):
			return (right_low,right_high,right_sum)
		else:
			return (cross_low,cross_high,cross_sum)
if __name__ == '__main__':
	A=[13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
	print FIND_MAXIMUM_SUB_ARRAY(A,0,len(A)-1)