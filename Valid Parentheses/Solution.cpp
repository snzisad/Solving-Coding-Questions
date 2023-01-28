#include<iostream>
#include<vector>
#include<string>
#include <bits/stdc++.h>

using namespace std;

bool isValid(string s) {
    int s_length = s.length();
    if(s_length == 0) return true;
    if(s_length%2 == 1) return false;

    vector<char> brac1 = {'(', '{', '['};
    vector<char> brac2 = {')', '}', ']'};
    vector<int> positions = {};

    for(int i=0; i<s_length; i++){
        char x = s[i];
        auto it = find(brac1.begin(), brac1.end(), x);

        if(it != brac1.end()){
           positions.push_back((it-brac1.begin()));
        }
        else if(positions.size()>0){
            auto it = find(brac2.begin(), brac2.end(), x);

            if(it != brac2.end() && positions.back() == (it-brac2.begin())){
                positions.pop_back();
            }
            else{
                return false;
            }
        }
        else{
            return false;
        }
    }

    if(!positions.empty()){
        return false;
    }

    return true;
}

int main(){
    cout << isValid("()[]{}") << endl;
    return 0;
}