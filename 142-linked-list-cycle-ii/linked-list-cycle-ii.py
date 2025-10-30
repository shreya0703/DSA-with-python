# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        # Phase 1: Detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:  # cycle detected
                break
        else:
            return None  # no cycle

        # Phase 2: Find start of cycle
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow  
        