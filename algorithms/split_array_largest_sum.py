# Given an array nums which consists of non-negative integers and an 
# integer m, you can split the array into m non-empty continuous 
# subarrays.
#
# Write an algorithm to minimize the largest sum among these m 
# subarrays.
#
# Ex:
# Input: nums = [7, 2, 5, 10, 8], m = 2
# Output: 18
# Explanation: There are four ways to split nums into two subarrays. 
# The best way is to split it into [7, 2, 5] and [10, 8], where the 
# largest sum among the two subarrays is only 18.
#
# Constraints:
#   * 1 <= nums.length <= 1000 
#   * 0 <= nums[i] <= 10^6
#   * 1 <= m <= min(50, nums.length)

def split_array(nums: list[int], m: int) -> int:
    min_result, max_result = 0,0
    for num in nums:
        max_result += num
        if num > min_result:
            min_result = num
    
    final_result = float('inf')
    while min_result <= max_result:
        mid = (min_result + max_result) // 2
        if is_possible(mid, nums, m):
            final_result = mid
            max_result = mid-1
        else:
            min_result = mid+1
    
    return final_result

def is_possible(x, nums, m):
    num_subarrays = 1
    subarray_sum = 0
    for num in nums:
        if (num + subarray_sum) <= x:
            subarray_sum += num
        else:
            num_subarrays += 1
            subarray_sum = num
        
    return (num_subarrays <= m)