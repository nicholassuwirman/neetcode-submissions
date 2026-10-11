# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# list1 = [1,2,4]
# list2 = [2,3,5]
# list1 <= list2
# listOutput = [1,2,2,3,4,5]

#    dummy (stays!)
#    tail -----will move to the end/tail of the list----->
#      |
#     [0] -> None          (the dummy node, its value is never used)
# why not directly use listOutput instead of using tail?
# bcs at the end, listOutput is a pointer that still needs to point at the head of our return linked list
# and tail will point at the end of our list
# so essentially it's just two pointers with fancier name

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        curr1 = list1
        curr2 = list2

        # while both lists' pointer is not at the end
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                tail.next = curr1
                curr1 = curr1.next
            else:
                tail.next = curr2
                curr2 = curr2.next
            tail = tail.next
        
        if curr1:
            tail.next = curr1
        else:
            tail.next = curr2

        return dummy.next

