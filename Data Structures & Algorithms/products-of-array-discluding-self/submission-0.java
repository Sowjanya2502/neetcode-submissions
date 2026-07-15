class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] arrList = new int[nums.length];
        int right =1;
        int left =1;
        for(int i =0; i<nums.length; i++){
            arrList[i]=left;
            left = left*nums[i];
        }
        for(int i=nums.length-1; i>=0; i--){
            arrList[i]=arrList[i]*right;
            right = right *nums[i];
        }
        return arrList;
    }
    
}  
