#include <iostream>  
using namespace std;  

string addBinary(string a, string b){int i = a.size() - 1, j = b.size() - 1, carry = 0;
        string s = "";
        while(i >= 0 || j >= 0 || carry){
            int sum = (i < 0 ? 0 : a[i--] - '0') + (j < 0 ? 0 : b[j--] - '0') + carry;
            s = to_string(sum % 2) + s;
            carry = sum / 2;
        }
        return s;
}

int main() {  
    cout << addBinary("1010", "1011");
    return 0;
}  