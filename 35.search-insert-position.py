#
# @lc app=leetcode id=35 lang=python
#
# [35] Search Insert Position
#
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        i = 0
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if nums[i] < target:
                continue
            if nums[i] > target:
                return i 
        return len(nums)
            
         
        

