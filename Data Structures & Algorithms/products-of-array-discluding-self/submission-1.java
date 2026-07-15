class Solution {
    public int[] productExceptSelf(int[] nums) {
       int[] arrList = new int[nums.length];
       int left = 1;
       int right =1;
       for(int i=0; i<nums.length; i++){
        arrList[i]=left;
        left=left*nums[i];
       }
       for(int j=(nums.length)-1; j>=0; j--){
        arrList[j]=arrList[j]*right;
        right = right*nums[j];
       }
       return arrList;
    }
    
}  
