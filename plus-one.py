# https://leetcode.com/problems/plus-one/
# converting list into string, make it an integer then add 1 to it and then make it a list by iterating over the str of that value

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=[str(x) for x in digits]
        a=int("".join(s))+1
        l=[i for i in str(a)]
        return l
