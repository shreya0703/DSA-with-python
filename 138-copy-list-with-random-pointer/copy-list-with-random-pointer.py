# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Step 1: Clone each node and insert it right after the original node
        temp = head
        while temp:
            new_node = Node(temp.val)
            new_node.next = temp.next
            temp.next = new_node
            temp = new_node.next

        # Step 2: Assign random pointers for the cloned nodes
        temp = head
        while temp:
            if temp.random:
                temp.next.random = temp.random.next
            temp = temp.next.next

        # Step 3: Separate the cloned list from the original list
        temp = head
        copy_head = head.next
        copy_temp = copy_head

        while temp:
            temp.next = temp.next.next
            if copy_temp.next:
                copy_temp.next = copy_temp.next.next
            temp = temp.next
            copy_temp = copy_temp.next

        return copy_head
