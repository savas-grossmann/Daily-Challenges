class maxSubArray {

    /*
        https://leetcode.com/problems/maximum-subarray/
        given an int array find the biggest continous Subarray

        Easy Solution in o(n) which goes trough the array and uses temp to get
        the biggest subarray. Temp starts with 0 and then gets the first nums element.
        if sum is smaller than sum = temp. If temp is bigger then 0 we go to the next
        element of nums and add that too. If temp < 0 we set it to 0 because it will make
        the next element of the array smaller.
     */

    public int maxSubArray(int[] nums){
        int sum = Integer.MIN_VALUE;
        int temp = 0;
        for(int i = 0; i < nums.length; i++){
            temp = temp + nums[i];
            if(sum < temp) sum = temp;
            if(temp < 0) temp = 0;
        }
        return sum;
    }

}