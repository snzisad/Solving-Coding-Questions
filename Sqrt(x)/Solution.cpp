#include<vector>
#include<iostream>

using namespace std;

int mySqrt(int x) {
    if(x == 0) return 0;
    long r = x;
    while (r > x/r){
        r = (r + x/r) / 2;
        cout << r << endl;
    }
    return r;
}

int main(){
    cout << mySqrt(8) << endl;
    return 1;
}