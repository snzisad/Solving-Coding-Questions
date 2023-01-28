#include<iostream>
#include<vector>

using namespace std;

string longestCommonPrefix(vector<string>& strs) {
    string prefix = "";
    string temp_prefix = "";

    if(strs.size() <= 0){
        return prefix;
    }

    string first_string = strs[0];

    for(int i=0; i<first_string.length(); i++){
        temp_prefix = prefix+first_string[i];

        for(int j=1; j<strs.size(); j++){
            if(strs[j].rfind(temp_prefix, 0) != 0){
                return prefix;
            }
        }

        prefix = temp_prefix;
    }

    return prefix;
}

int main(){
    vector<string> inputs = {"flower","flow","flight"};
    cout << longestCommonPrefix(inputs) << endl;
    return 0;
}