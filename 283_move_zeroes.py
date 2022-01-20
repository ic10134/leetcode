#Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#Note that you must do this in-place without making a copy of the array.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        for j in range(len(nums)):
            if (nums[j] != 0):
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums

#We use i to keep track of position of the first zero in the list (which changes as we go).
#We use j to keep track of the first non-zero value after the first zero (which is pointed by i).
#Each time we havei correctly points to a zero and j correctly points to the first non-zero after i, we swap the values that store at i and j.
#By doing this, we move zeros towards the end of the list gradually until j reaches the end.
