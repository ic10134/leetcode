#Given an array, rotate the array to the right by k steps, where k is non-negative.

class Solution:
    def reverse(self,nums:list, start:int,end:int) -> None:
        while start <= end:
            nums[start],nums[end] = nums[end],nums[start]
            start,end = start+1,end-1        
        
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        n = len(nums) - 1
        
        self.reverse(nums,0,n)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,n)