# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # empty or single or when k =0 
        if not head or not head.next or k == 0:
            return head

        # step 1 : find length and tail node
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length +=1
        #make list crircular
        tail.next = head

        # compute rotations
        k = k % length

        steps_to_new_node = length - k

        # reach new tail node
        new_tail = head
        for _ in range(steps_to_new_node-1):
            new_tail = new_tail.next
         # Step 5: Set new head and break the circle
        new_head = new_tail.next
        new_tail.next = None

        return new_head

        