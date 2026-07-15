class Solution {

    public String encode(List<String> strs) {
        StringBuilder encodedString = new StringBuilder();
        for (String str : strs) {
            encodedString.append(str.length()).append("#").append(str);
        }
        return encodedString.toString();
    }

    public List<String> decode(String str) {
         List<String> strs = new ArrayList<>();
         int i =0;
         while(i<str.length()){
            int j=i;
            while(str.charAt(j)!='#')j++;
            int length = Integer.valueOf(str.substring(i,j));
            i=length+j+1;
            strs.add(str.substring(j+1,i));
         }
       return strs; 
    }
}
