#
# @lc app=leetcode id=21 lang=python
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (45.61%)
# Total Accepted:    531.2K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# Merge two sorted linked lists and return it as a new list. The new list
# should be made by splicing together the nodes of the first two lists.
# 
# Example:
# 
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
# 
# 
#
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        nlist = ListNode(None)
        ln = nlist
    
       
        while l1 or l2:
            if l1 and l2:
                if l1.val <= l2.val:
                    ln.next = l1
                    l1 = l1.next
                else:
                    ln.next = l2
                    l2 = l2.next
            elif l1:
                ln.next = l1
                l1 = l1.next
            else:
                ln.next = l2
                l2 = l2.next
            ln = ln.next
        return nlist.next


