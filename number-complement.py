# https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        a=len(bin(num))-2
        b="1"*a
        b=int(b,2)
        return num^b
