class Solution {
public:
    int singleNumber(vector<int>& nums) {
        
        map<int, int>pairs = {};
        for(int i=0; i<nums.size(); i++){
            if(pairs.count(nums[i])){
                pairs[nums[i]] += 1;
            }
            else{
                pairs[nums[i]] = 1;
            }
        }

        for (auto &p : pairs ){
            if(p.second%2 != 0){
                return p.first;
            }
        }

        return 0;
    }
};