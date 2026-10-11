# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# idea here to use slow and fast pointer
# slow move once, fast move twice
# compare them , because in a cycle they will eventually meet
# a cycle either exist (index=1) or doesnt exist (index=-1)
# so maybe while fast != None:, because if fast hits None, it means that there's no cycle

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        # why check the fast and not the slow?
        # bcs fast is always faster than slow, so if fast passes then slow will too
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

