# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ptr1 = head
        ptr2 = head.next

        while(ptr2 != None):

            gcd_num = math.gcd(ptr1.val, ptr2.val)
            new_node = ListNode(gcd_num, ptr1.next)
            ptr1.next = new_node

            ptr1 = ptr2
            ptr2 = ptr2.next
        
        return head

            

