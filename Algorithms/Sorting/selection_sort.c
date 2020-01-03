#include <stdio.h>

void swap(int *x,int *y){
    int tmp = *x;
    *x = *y;
    *y = tmp;    

}

void selection_sort(int *a, int n,int x){
    int min_index,i,j;
    for(i = 0; i < x; i++){
        min_index = i;
        for(j = i+1; j < n; j++){
            if (a[j] < a[min_index]){
                min_index = j;
            }
        }
        swap(&a[min_index],&a[i]);   
    }    
}

void print_array(int *a, int n){
    int i;
    for(i = 0; i < n; i++)
        printf("%d ",a[i]);


}
int main(){    
    int n,x,i,a[100];
    scanf("%d %d",&n,&x);
    for(i = 0; i < n; i++)
        scanf("%d",&a[i]);
    selection_sort(a,n,x);
    print_array(a,n);    
}
