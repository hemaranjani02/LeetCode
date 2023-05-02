# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        
        count = 0
        
        fast = head
        while fast != None:
            fast = fast.next
            count = count + 1
        
        mid = count // 2 + 1
        
        slow = head
        for i in range(mid, count):
            slow = slow.next
            
        return slow




obj=Solution()
_list=ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
mid_node=obj.middleNode(_list)
while mid_node != None:
    print(mid_node.val)
    mid_node=mid_node.next