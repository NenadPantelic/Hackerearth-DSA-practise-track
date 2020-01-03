#include <stdio.h>
#include <iostream>

using namespace std;

int linear_search(int *array, int n, int element){
	for (int i = 0; i < n; i++)
		if (array[i] == element)
			return i;
	return -1;

}
void insertion_sort_indexing(int *a, int n, int *b){

    int tmp,j;
    for(int i = 0; i < n; i++){   
	    tmp = a[i];
	    j = i;
	    while(j > 0  && a[j-1] > tmp){
		    a[j] = a[j-1];    
		    j--;
	    }
	    a[j] = tmp;
    }
    
    for (int i = 0; i < n; i++)
        b[i] = linear_search(a,n,b[i]) + 1;   

}

void print_array(int *a, int n){
    for(int i = 0; i < n; i++)
        cout << a[i] << " ";
}

int main(){
  int n,i,a[100],b[100];
    cin >> n;
    for(i = 0; i < n; i++){
        cin >> a[i];
	    b[i] = a[i];
    }
    insertion_sort_indexing(a,n,b);
    print_array(b,n);  
}

