import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap old_values = new HashMap<Integer, Integer>();
        
        for(int i=0; i<nums.length; i++){
            if(old_values.containsKey(target-nums[i])){
                int pos = (int)old_values.get(target-nums[i]);
                return new int[]{pos, i};
            }
            else{
                old_values.put(nums[i], i);
            }
        }
        return new int[]{};
    }

    public static void main(String args[]){
        int[] nums = new int[]{2,7,11,15};
        int target = 9;
        System.out.println(new Solution().twoSum(nums, target));
    }
}