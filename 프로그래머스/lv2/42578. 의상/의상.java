import java.util.*;
class Solution {
    public int solution(String[][] clothes) {
        HashMap<String, Integer> map = new HashMap<>();
        for (String[] arr : clothes) {
            map.put(arr[1], map.getOrDefault(arr[1], 0) + 1);
        }
        int ans = 1;
        for (String i : map.keySet()) {
            ans *= (map.get(i)+1);
        }
        return ans-1;
    }
}