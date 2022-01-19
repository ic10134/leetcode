# Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start_index, end_index = 0, len(nums)-1

        while start_index <= end_index:
            midpoint = start_index + (end_index - start_index) // 2
            midpoint_value = nums[midpoint]
            if midpoint_value == target:
                return midpoint
            if target < midpoint_value:
                end_index = midpoint - 1            
            else:
                start_index = midpoint + 1
        return start_index
