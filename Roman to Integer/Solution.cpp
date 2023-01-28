#include<iostream>
#include<string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int romanToInt(string s) {
    vector<char> r = {'I', 'V', 'X', 'L', 'C', 'D', 'M'};
    int m[] = {1, 5, 10, 50, 100, 500, 1000};
    int y = 0;
    int i = 0;
    int s_length = s.length();

    while(i<s_length){
        auto it = find(r.begin(), r.end(), s[i]);
        int pos = -1;

        if(it != r.end()){
            pos = it-r.begin();
        }

        if(i == s_length-1){
            y = y+m[pos];
            break;
        }
        else{

            auto it = find(r.begin(), r.end(), s[i+1]);
            int pos2 = -1;

            if(it != r.end()){
                pos2 = it-r.begin();
            }

            if((pos == 0 && (pos2 == 1 || pos2 == 2)) || (pos == 2 && (pos2 == 3 || pos2 == 4)) || (pos == 4 && (pos2 == 5 || pos2 == 6))){
                y = y + (m[pos2] - m[pos]);
                i = i+2;
            }
            else{
                y = y+m[pos];
                i = i+1;
            }
        }
    }

    return y;

}

int main(){
    cout << romanToInt("LVIII") << endl;
    return 0;
}