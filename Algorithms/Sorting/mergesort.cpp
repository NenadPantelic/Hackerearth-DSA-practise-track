
// Write your code here
#include <bits/stdc++.h>
using namespace std;

long long counter = 0;

void merge(long long arr[], int l, int mid, int r){

    int i = 0, j = 0;

    int lenA = mid-l+1;
    int lenB = r-mid;
    int k = l;

    long long arrA[lenA], arrB[lenB];
    for(i = 0; i < lenA; i++) arrA[i] = arr[l+i];
    for(j = 0; j < lenB; j++) arrB[j] = arr[mid+1+j];
    i = 0; j = 0;

    while (i < lenA && j < lenB){

        if(arrA[i] <= arrB[j]){
            arr[k++] = arrA[i++];
        } else{
            arr[k++] = arrB[j++];
            counter += (lenA - i);
        }
    }

    while(i < lenA){
        arr[k++] = arrA[i++];
    }

    while(j < lenB){
        arr[k++] = arrB[j++];
    }


}

void merge_sort(long long arr[], int l, int r){

    int mid;
    if (l < r){

        mid = l+ (r - l) / 2;
        merge_sort(arr, l, mid);
        merge_sort(arr, mid+1, r);
        merge(arr, l, mid, r);

    }

}
int main(){

    std::ios_base::sync_with_stdio(false);
    long long n;
    cin >> n;
    long long arr[n];
    for (int i = 0; i < n; i++){
        cin >> arr[i];
    }
    merge_sort(arr, 0, n-1);
    cout << counter << endl;


}
