#Given an integer array nums sorted in non-decreasing order,
#return an array of the squares of each number sorted in non-decreasing order.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        begin_index, end_index = 0, len(nums) -1
        while begin_index <= end_index:
            if nums[begin_index] * nums[begin_index] > nums[end_index] * nums[end_index]:
                res.append(nums[begin_index] * nums[begin_index])
                begin_index = begin_index+1
            else:
                res.append(nums[end_index] * nums[end_index])
                end_index = end_index - 1
        return res[::-1]