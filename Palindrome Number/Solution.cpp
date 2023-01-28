#include <iostream>  
#include<string>
using namespace std;  

bool isPalindrome(int x) {
    if(x<0) return false;
    if(x==0) return true;

    string num = to_string(x);

    int i = 0;
    int j = num.length()-1;

    while(i<j){
        if(num[i] != num[j]) return false;
        i++;
        j--;
    }

    return true;

}


int main() {  
    cout << "Result: " << isPalindrome(121) << endl;
    return 0;
}  