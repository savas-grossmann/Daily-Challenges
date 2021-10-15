import java.util.HashMap;

public class TwoSum {
    /*
        https://leetcode.com/problems/two-sum/
        given an int array and a target. Choose 2 ints out of the array
        which add up to the target.
     */

    /*
        As usual just check every single possible Solution and return+
        the correct one.
        O(n^2)
     */
    public int[] twoSum_bruteForce(int[] nums, int target) {
        int[] erg = new int[2];
        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = i + 1; j != nums.length; j++){
                if(nums[i] + nums[j] == target) {
                    erg[0] = i;
                    erg[1] = j;
                    break;
                }
            }
        }
        return erg;
    }

    /*
        We calculate the rest of our target minus the i-th num.
        Then we check if we have the difference in our HashMap. If we have
        we can return the indices. Else we add the new found number into
        out hashmap for the next turns.
        O(n)
     */
    public int[] twoSum(int[] nums, int target){
        int[] erg = new int[2];
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++){
            int rest = target - nums[i];
            if(map.containsKey(rest)) {
                erg[0] = i;
                erg[1] = map.get(rest);
                return erg;
            } else {
                map.put(nums[i], i);
            }
        }
        return new int[]{-1, -1};
    }
}