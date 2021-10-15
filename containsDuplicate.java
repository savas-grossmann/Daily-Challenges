import java.util.HashSet;
import java.util.Set;

class containsDuplicate {

    /*
        https://leetcode.com/problems/contains-duplicate/
        Check an array and return true if there is atleast one duplicate num.
        Sets cant contain duplicates, so we can just add every element of nums
        to a set and check the sizes. If the set is smaller then there are duplicates.

     */

    public boolean containsDuplicate_normal(int[] nums){
        Set<Integer> numbers = new HashSet<>();
        for(int i: nums){
            numbers.add(i);
        }
        /*
        If the size is smaller there are duplicates, if its equal
        (or bigger which is not possible) there are no duplicates.
        */
        if(numbers.size() < nums.length){
            return true;
        } else {
            return false;
        }
    }

    public boolean containsDuplicate_short(int[] nums){
        Set<Integer> numbers = new HashSet<>();
        /*
            set.add returns false if it didnt add the element i to the set so
            i is already in the set.
         */
        for(int i: nums){
            if(!numbers.add(i)) return true;
        }
        return false;
    }

}