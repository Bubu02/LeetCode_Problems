import heapq
from typing import List, Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        
        heap = []
        count = 0  # Serves as a unique tie-breaker for identical node values
        
        # Initialize the heap with the head node of each non-empty linked list
        for l in lists:
            if l:
                heapq.heappush(heap, (l.val, count, l))
                count += 1
                
        # Extract the minimum node and push the next node from that list
        while heap:
            val, _, node = heapq.heappop(heap)
            
            current.next = node
            current = current.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, count, node.next))
                count += 1
                
        return dummy.next