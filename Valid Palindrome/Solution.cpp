#include<string>
#include<iostream>

using namespace std;

bool isPalindrome(string s) {
    int i=0, j=s.size()-1;
    while(i<j){
        if(isalnum(s[i]) && isalnum(s[j])){
            if(tolower(s[i]) != tolower(s[j])){
                return false;
            }
            else{
                i++;
                j--;
                continue;
            }
        }
        if(!isalnum(s[i])) i++;
        if(!isalnum(s[j])) j--;
    }

    return true;

}

int main(){
    cout << isPalindrome("A man, a plan, a canal: Panama") << endl;
    return 0;
}