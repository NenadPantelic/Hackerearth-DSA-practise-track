#include <stdio.h>

void swap_num(int *x,int *y){

    int tmp = *x;
    *x = *y;
    *y = tmp;


}

int bubble_sort(int *a, int n){

    int count = 0,i,j;
    for(i = 0; i < n-1; i++){
	    for(j = 0; j < n-i-1; j++){
           if (a[j] > a[j+1]){
                swap_num(&a[j],&a[j+1]);           
		        count++;
           }
        }
    }
    return count;
}


int main()
{

    int n,i,a[100];
    scanf("%d",&n);
    for(i = 0; i < n; i++)
        scanf("%d",&a[i]);
    printf("%d\n",bubble_sort(a,n));
    
    return 0;
}


