# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1 -> 2 -> 4 -> Null
#                curr1

# 1 -> 3 -> 5 -> Null
#         curr2

# dummy -> 1 -> 1 -> 2 -> 3 -> 4
#         tail
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        curr1 = list1
        curr2 = list2
        tail = dummy

        while curr1 and curr2:
            if curr2.val <= curr1.val:
                tail.next = curr2
                curr2 = curr2.next
            else:
                tail.next = curr1
                curr1 = curr1.next
            tail = tail.next
        
        if curr1:
            tail.next = curr1
        elif curr2:
            tail.next = curr2
        return dummy.next
            

        