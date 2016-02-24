public class InsertionSort{

	public static int[] insertionSort(int A[],int len){
		int i,key;
		for(int j=1;j<len;j++){
			key = A[j];
			i = j-1;
			while(i>=0 && A[i]>key){
				A[i+1]=A[i];
				i -=1;
			}
			A[i+1]=key;
		}
		return A;
	}
	public static void printArray(int A[],int len){
		for(int i=0;i<len;i++){
			System.out.print(A[i]);
			System.out.print(", ");
		}
		System.out.println();
	}
	public static void main(String args[]){
		int[] A = {5,2,4,6,1,3};
		int l = 6;
		System.out.print("Before:-\t");printArray(A,l);
		insertionSort(A,l);
		System.out.print("After:- \t");printArray(A,l);
	}
}