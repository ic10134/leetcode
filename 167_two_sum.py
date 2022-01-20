# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
# find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] 
# where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        si, ei = 0, len(numbers) - 1
        while si <= ei:
            if target < numbers[si] + numbers[ei]:
                ei-=1
            elif target > numbers[si] + numbers[ei]:            
                si+=1            
            elif target == numbers[si] + numbers[ei] and si != ei:
                return [si+1, ei+1]
            else:
                return [-1,-1]
