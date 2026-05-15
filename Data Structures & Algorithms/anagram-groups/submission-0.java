class Solution {

    public List<List<String>> groupAnagrams(String[] strs) {
        Map<Map<Character,Integer>, ArrayList<String>> lists = new HashMap<>();
        int length_strs = strs.length;
        for (int i = 0; i < length_strs; ++i){
            int length_word = strs[i].length();
            Map<Character,Integer> count = new HashMap<>();
            String word = strs[i];
            for (int j = 0; j < length_word; ++j){
                Character c = word.charAt(j);
                count.put(c, count.getOrDefault(c, 0) + 1);
            }
            ArrayList<String> temp = lists.getOrDefault(count, new ArrayList<>());
            temp.add(strs[i]);
            lists.put(count, temp);
            

        }

        return new ArrayList<>(lists.values());    }
}
