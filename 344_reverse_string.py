#Write a function that reverses a string. The input string is given as an array of characters s.
#You must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        si, ei = 0, len(s) - 1
        while si <= ei:
            s[si], s[ei] = s[ei], s[si]
            si, ei = si + 1, ei - 1
        return s