# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# just watch the solution video

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Before the cut, on 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6, slow is at 3:
        #   0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
        #                 slow
        
        # second = slow.next first saves a variable pointing at 4, so you don’t lose the second half:
        # 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
        #               slow second

        # Then slow.next = None overwrites the arrow coming out of 3:
        # 0 -> 1 -> 2 -> 3 -> None        4 -> 5 -> 6 -> None
        #               slow             second

        # prev is the starting point for the new reversed linked list, ready to be attached w/ new nodes
        # None
        # prev

        # reverse second half
        second = slow.next
        slow.next = None
        prev = None     

        # (2. second.next = prev)
        # None <-   4     ->    5    ->   6   ->  None
        # prev    second       nxt (1. nxt = second.next)
        #   |        |------->second (4. second = nxt)
        #   |
        #   |------>prev (3. prev = second)
        while second:
            nxt = second.next
            second.next = prev  # current/second pointer points to the prev pointer
            prev = second
            second = nxt

        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


