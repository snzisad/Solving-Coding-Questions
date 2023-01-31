#include<vector>
#include<iostream>

using namespace std;

int searchInsert(vector<int>& nums, int target) {
    
    if(nums[0]>=target) return 0;

    if(nums.back()<target) return nums.size();

    int start_pos = 0;
    int end_pos = nums.size();
    int mid_pos = 0;

    while(1){
        mid_pos = (int)((start_pos+end_pos)/2);
        if(mid_pos > 0 && nums[mid_pos-1]<target && nums[mid_pos]>=target){
            
            return mid_pos;
        }
        else if(nums[mid_pos]<target){
            start_pos = mid_pos+1;
        }
        else{
            end_pos = mid_pos - 1;
        }
    }
}

int main(){
    vector<int> nums = {1,3,5,6};
    cout << searchInsert(nums, 2) << endl;
    return 0;
}