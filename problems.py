from typing import List

class Solution:
    # 1. Two Sum
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i, j]
                
    # 9. Palindrome Number
    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            return False
        if (x < 10):
            return True
        x_str = str(x)
        x_len = len(x_str)
        if (x_str[x_len-1] == '0'):
            return False
        for i in range(x_len//2):
            if (x_str[i] != x_str[x_len-1-i]):
                return False
        return True
    
    # 13. Roman to Integer
    def romanToInt(self, s: str) -> int:
        symbol_mapping = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        sum=0
        for i in range(len(s)-1):
            if (symbol_mapping[s[i]] >= symbol_mapping[s[i+1]]):
                sum = sum + symbol_mapping[s[i]]
            else:
                sum = sum - symbol_mapping[s[i]]
        sum = sum + symbol_mapping[s[len(s)-1]]
        return sum
    