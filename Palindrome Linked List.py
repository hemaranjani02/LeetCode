# Definition for singly-linked list.
class ListNode(object)
    def __init__(self, val=0, next=None)
        self.val = val
        self.next = next
class Solution(object)
    def isPalindrome(self, head)
        
        type head ListNode
        rtype bool
        
        stack=[]
        temp = head
        ispal = True

        while temp!=None
            stack.append(temp.val)
            temp=temp.next
        
        while head!=None
            i=stack.pop()
            if head.val==i
                ispal=True
            else
                ispal=False
                break

            head=head.next

        return ispal

        