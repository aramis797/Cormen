/*
Insertion sort implementation
It takes two arguments i.e array and its length
and sorts the array.
*/

#include <stdio.h>
void Insertion(int A[],int n){
	int key,temp,j;
	for(int i=1;i<n;i++){
		key=A[i];
		j=i-1;
		while(j >= 0 && A[j]>A[j+1]){
			temp=A[j];A[j]=A[j+1];A[j+1]=temp;
			j-=1;
		}
		A[j+1]=key;
	}
}
int main(){
	int A[5]={5,4,3,2,1};
	for(int i=0;i<5;i++) printf("%d ",A[i]);printf("\n");
	Insertion(A,5);
	for(int i=0;i<5;i++) printf("%d ",A[i]);printf("\n");
}