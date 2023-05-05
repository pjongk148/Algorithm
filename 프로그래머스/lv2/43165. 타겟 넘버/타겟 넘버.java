import java.util.*;
class Solution {
    public int solution(int[] numbers, int target) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(0);
        for (int idx=0;idx< numbers.length;idx++) {
            for (int i = 0; i < Math.pow(2,idx); i++) {
                Integer tmp = queue.poll();
                queue.add(tmp + numbers[idx]);
                queue.add(tmp - numbers[idx]);
            }

        }
        return Collections.frequency(queue,target);
    }
}