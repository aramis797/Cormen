#include <stdio.h>
void Merge(int A[],int p,int q,int r){
	int n1 = q-p+1;
	int n2 = r-q;
	int L[n1],R[n2];
	for(int i=0;i<n1;i++) L[i] = A[p+i];
	for(int j=0;j<n2;j++) R[j] = A[q+j+1];
	int li=0,ri=0;
	for(int k=p;k<r+1;k++){
		if(li < n1 && ri < n2){
			if(L[li] <= R[ri]) A[k] = L[li++];
			else A[k] = R[ri++];
		}
		else{
			if(li == n1) A[k] = R[ri++];
			else A[k] = L[li++];
		}
	}
}
void mergeSort(int A[],int p,int r){
	if (p<r){
		int q = (p+r)/2;
		mergeSort(A,p,q);
		mergeSort(A,q+1,r);
		Merge(A,p,q,r);
	}
}
int main(){
	int A[9]={5,4,3,2,1,6,8,7,9};
	for(int i=0;i<9;i++) printf("%d ",A[i]);printf("\n");
	mergeSort(A,0,8);
	for(int i=0;i<9;i++) printf("%d ",A[i]);printf("\n");
	}