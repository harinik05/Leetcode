import java.util.*;

class Solution {
    public int leastInterval(char[] tasks, int n) {
        // Step 1: Use a hashmap to count the frequency of each task
        Map<Character, Integer> taskCount = new HashMap<>();
        for (char task : tasks) {
            taskCount.put(task, taskCount.getOrDefault(task, 0) + 1);
        }

        // Step 2: Use a max heap (priority queue) to sort tasks by frequency
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        for (int count : taskCount.values()) {
            maxHeap.add(count);
        }

        // Step 3: Queue to manage cooldowns
        Queue<int[]> cooldownQueue = new LinkedList<>(); // Pair of (remainingCount, availableTime)
        int time = 0;

        // Step 4: While we have tasks left to process
        while (!maxHeap.isEmpty() || !cooldownQueue.isEmpty()) {
            time++; // Increment time

            // a. If there are tasks available in the heap, process one task
            if (!maxHeap.isEmpty()) {
                int currentTaskCount = maxHeap.poll() - 1; // Pop the highest frequency task
                if (currentTaskCount > 0) {
                    cooldownQueue.offer(new int[] { currentTaskCount, time + n }); // Put it into cooldown
                }
            }

            // b. Check if any task in the cooldown queue can be added back to the heap
            if (!cooldownQueue.isEmpty() && cooldownQueue.peek()[1] == time) {
                maxHeap.offer(cooldownQueue.poll()[0]); // Task's cooldown is finished
            }
        }

        return time; // The total time to complete all tasks
    }
}
