# https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=""
        for i in s:
            if i.isalpha():
                if i.isupper():
                    a+=i.lower()
                else:
                    a+=i
            if i.isnumeric():
                a+=i
        return a==a[::-1]
                
