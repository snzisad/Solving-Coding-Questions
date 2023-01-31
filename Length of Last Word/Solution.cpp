#include<iostream>

using namespace std;

int lengthOfLastWord(string s) {
    int counter = 0;
    int last_length = 0;

    for(int i=0; i<s.size(); i++){
        if(s[i] != ' '){
            counter++;
        }
        else{
            if(counter>0){
                last_length = counter;
            }
            counter = 0;
        }
    }

    if(counter>0){
        last_length = counter;
    }

    return last_length;
}