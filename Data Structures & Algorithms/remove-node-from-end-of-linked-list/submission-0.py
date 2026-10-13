# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Big idea:
# 1. reverse the list, now you get the back pointer
# 2. remove the nth from back (which now can .next to iterate)
# 3. reverse back the list

#   1  ->  2  ->  3  ->  4 -> None
# None <- 1 <- 2 <- 3 <- 4 
# prev   curr  tmp
# None <- 1 <- 2 <- 3 <- 4 
#                       prev   curr  tmp

# curr = prev (careful!)
# None
# tmp1
#   4  ->  3  ->  2  ->  1 -> None
#  curr
# counter = 0
#   4  ->  3  ->  2  ->  1 -> None
#  tmp1   curr
# counter = 1
#   4  ->  3  ->  2  ->  1 -> None
#         tmp1   curr
# counter = 2

#   4  ->  3  ->  2  ->  1 -> None
#         tmp1   curr   tmp2
# tmp1.next = tmp2
#   4  ->  3  ->  1 -> None
#         tmp1   tmp2

#   4  ->  3  ->  1 -> None
#headRev  tmp
# None <- 4 -> 3 -> 1 -> None
# res    
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        dummy = ListNode(0, prev)
        tmp1 = dummy
        counter = 0
        while counter < n - 1:
            tmp1 = tmp1.next
            counter += 1
        tmp1.next = tmp1.next.next
        

        res = None
        headReversed = dummy.next
        while headReversed:
            tmp = headReversed.next
            headReversed.next = res
            res = headReversed
            headReversed = tmp
        
        return res





        
