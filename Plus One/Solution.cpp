#include<vector>
#include<iostream>

using namespace std;

vector<int> plusOne(vector<int>& digits) {
    vector<int> new_digits = {};
    int carry = 1;
    int sum1 = 0;

    for(int i=digits.size()-1; i>=0; i--){
        sum1 = digits[i] + carry;
        if(sum1>9){
            new_digits.insert(new_digits.begin(), 0);
            carry = 1;
        }
        else{
            new_digits.insert(new_digits.begin(), sum1);
            carry = 0;
        }
    }

    if(carry>0){
        new_digits.insert(new_digits.begin(), carry);
    }

    return new_digits;

}

int main(){
    vector<int> nums = {4,3,2,1};
    vector<int> output = plusOne(nums);

    for(int i=0; i<output.size(); i++){
        cout << output[i] << endl;
    }

    return 0;
}