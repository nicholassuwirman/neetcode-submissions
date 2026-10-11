# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# head is the first node of the linked list
# From it you can reach every other node by following .next

# two pointers, iterative solution
# null -> 1 -> 2 -> 3 -> null
# prev   curr
# null <- 1 -> 2 -> 3 -> null
#        prev curr
# null <- 1 <- 2 -> 3 -> null
#             prev curr
# null <- 1 <- 2 <- 3   null
#                  prev curr
# as we're setting the next curr.next pointer to the left
# the last pointer (3) points to the left, hence curr is now pointing to null/None

# PS: None is null equivalent in python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        #or simply, while curr:
        while curr != None:
            nxt = curr.next
            curr.next = prev # set the next curr pointer to the left of the node
            prev = curr
            curr = nxt
        return prev