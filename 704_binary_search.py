#Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1. 
# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def search(self, nums:list[int], target:int) -> int:
        begin_index, end_index = 0, len(nums) -1

        while begin_index <= end_index:
            midpoint = begin_index + (end_index - begin_index) // 2
            midpoint_value = nums[midpoint]

            if midpoint_value == target:
                return midpoint

            elif target < midpoint_value:
                end_index = midpoint - 1
            
            else:
                begin_index = midpoint + 1
            
        return -1