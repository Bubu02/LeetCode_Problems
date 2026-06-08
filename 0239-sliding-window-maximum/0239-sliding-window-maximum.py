from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
            
        q = deque() # Will store indices of elements
        result = []
        
        for i in range(len(nums)):
            # 1. Remove indices that are out of the current sliding window's bounds
            if q and q[0] < i - k + 1:
                q.popleft()
                
            # 2. Maintain monotonic property: remove elements smaller than the current element
            while q and nums[q[-1]] < nums[i]:
                q.pop()
                
            # 3. Append current element's index to the queue
            q.append(i)
            
            # 4. Once the window reaches size k, append the max (front of queue) to our results
            if i >= k - 1:
                result.append(nums[q[0]])
                
        return result