# Rotate List
'''
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or head.next==None:
            return head
        
        n = 0
        
        temp = head
        
        while temp:
            temp = temp.next
            n+=1
        
        rot = n-k%n
        
        if rot == 0 or rot == n:
            return head
        
        st = head
        temp = head
        i=0
        while temp:
            i+=1
            if i==rot:
                head = temp.next
                temp.next = None
                break
                
            temp = temp.next
            
        temp = head
        while temp.next:
            temp = temp.next
            
        temp.next = st
        return head     
        
