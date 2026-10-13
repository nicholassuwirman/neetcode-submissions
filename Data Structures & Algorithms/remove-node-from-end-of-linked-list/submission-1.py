# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# dummy node technique
# two pointers technique
# use dummy node, else we would get the wrong + 1 node of what we're trying to stich together! (try it)
# d -> 1 -> 2 -> 3 -> 4 -> 5 ->Null
#                l              r

# if we dont use dummy node
# 1 -> 2 -> 3 -> 4 -> 5 -> Null
#                l         r
# how do you suppose to attach 3 -> 5 then?

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        l = dummy
        r = head

        # calculate where the position of the r is
        counter = 0
        while counter < n and r:
            r = r.next
            counter += 1
        
        # iterate until r hits Null, then you'd get where the nth position is
        # bcs the distance of l and r is n
        while r:
            l = l.next
            r = r.next
        
        # delete the nth node from behind
        # i.e. attach the l node to the 2 next node of it
        l.next = l.next.next
        return dummy.next
        
        