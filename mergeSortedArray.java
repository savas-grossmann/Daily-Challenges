import java.util.Arrays;

public class mergeSortedArray {

    /*
        https://leetcode.com/problems/merge-sorted-array/
        Given two sorted Arrays merge them into one sorted array. Save the result in nums1.

        We start from the End and sort in reverse Order. We save the position we have right now
        and use that to correctly place the biggest int we have right now.
        Tail1 and Tail2 are used to check where we are in both arrays so we can check the ints we
        need to compare next.
    */

    public static void merge(int[] nums1, int m, int[] nums2, int n) {
        int position = m + n - 1;
        int tail1 = m - 1, tail2 = n - 1;

        while(tail1 >= 0 || tail2 >= 0){
            if(tail2 < 0 || (tail1 >= 0 && nums1[tail1] > nums2[tail2])){
                nums1[position] = nums1[tail1];
                position--;
                tail1--;
            } else {
                nums1[position] = nums2[tail2];
                position--;
                tail2--;
            }
        }
        //System.out.println(Arrays.toString(nums1));
    }

    /*
    public static void main(String[] args) {
        merge(new int[]{1,2,3,0,0,0}, 3, new int[]{2,5,6}, 3);
    }
    */

}
