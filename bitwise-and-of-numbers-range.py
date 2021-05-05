# https://leetcode.com/problems/bitwise-and-of-numbers-range/

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left==right:
            return left
        while right>left:
            right=right&(right-1)
        return right
