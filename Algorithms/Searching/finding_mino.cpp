#include<bits/stdc++.h>

using namespace std;

double func(double x){
    return 2*x*x-12*x+7;
}
double find_min(double start, double end){
    double l = start, r = end;
    double l1,l2;
    for(int i=0; i<50; i++) {
      l1 = (l*2+r)/3.;
      l2 = (l+2*r)/3.;
      if(func(l1) < func(l2)){
        r = l2;  
      } else {
        l = l1;
      }
    }
    return func(r);
}
