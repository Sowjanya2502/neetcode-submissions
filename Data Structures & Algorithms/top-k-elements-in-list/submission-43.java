class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int [] result = new int[k];
        Map <Integer, Integer> mp1 = new HashMap<>();
        for (int i=0; i<nums.length; i++){
            mp1.put(nums[i], mp1.getOrDefault(nums[i],0)+1);
        }
        PriorityQueue<int[]> minHeap = new PriorityQueue<>((a,b)-> a[0]-b[0]);        for (int i: mp1.keySet()){
            minHeap.add(new int[]{mp1.get(i), i});
            if (minHeap.size()>k) {
                minHeap.poll();
            }
        }
        for (int i=0; i<k; i++){
            
            int[] pair = minHeap.poll();
            result[i] = pair[1];
        }
        return result;
    }
}
