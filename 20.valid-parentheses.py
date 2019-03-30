#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (35.79%)
# Total Accepted:    537.2K
# Total Submissions: 1.5M
# Testcase Example:  '"()"'
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# 
# 
# Note that an empty string is also considered valid.
# 
# Example 1:
# 
# 
# Input: "()"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "()[]{}"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: "(]"
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: "([)]"
# Output: false
# 
# 
# Example 5:
# 
# 
# Input: "{[]}"
# Output: true
# 
# 
#
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        stack = []
        for i in s:
            if len(stack) < 2:
                stack.append(i)
                continue
        
            if (stack[-2] == '(' and stack[-1] == ')' )or\
                (stack[-2] == '[' and stack[-1] == ']')or\
                (stack[-2] == '{' and stack[-1] == '}'):
                stack.pop()
                stack.pop()
                stack.append(i)
            else:
                stack.append(i)
        if len(stack) == 2:
            if (stack[-2] == '(' and stack[-1] == ')' )or\
                (stack[-2] == '[' and stack[-1] == ']')or\
                (stack[-2] == '{' and stack[-1] == '}'):
                stack.pop()
                stack.pop()

        if len(stack) == 0 :
            return True
        else:
            return False
                


