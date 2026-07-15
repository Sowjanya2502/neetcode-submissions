class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer>dup = new HashSet<>();
        for(int i:nums){
            dup.add(i);
        }
        if(dup.size()==nums.length){
            return false;
        }else{
            return true;
        }
    }
}
