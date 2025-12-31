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
    
    # 14. Longest Common Prefix
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for word in strs:
            if (word == ""):
                return ""
            new_prefix = ""
            for i in range(min(len(prefix),len(word))):
                if (prefix[i] != word[i]):
                    if (i == 0):
                        return ""
                    else:
                        new_prefix = prefix[:i]
                        break
                else:
                    new_prefix = new_prefix + prefix[i]
            prefix = new_prefix
        return prefix
    
    # 20. Valid Parentheses
    def isValid(self, s: str) -> bool:
        open_brackets = ["(", "[", "{"]
        closed_brackets = [")", "]", "}"]
        stack = []

        for char in s:
            try:
                index = closed_brackets.index(char)
                if (len(stack) > 0 and stack.pop() == open_brackets[index]):
                    continue
                else:
                    return False

            except ValueError:
                stack.append(char)

        if (len(stack) == 0):
            return True
        else:
            return False
        
    