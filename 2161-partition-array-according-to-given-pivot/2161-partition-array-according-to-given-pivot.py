class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # Step 1: Create buckets to hold elements based on their relationship to the pivot
        less_than = []
        equal_to = []
        greater_than = []
        
        # Step 2: Iterate through the array and distribute the elements
        for num in nums:
            if num < pivot:
                less_than.append(num)
            elif num == pivot:
                equal_to.append(num)
            else:
                greater_than.append(num)
        
        # Step 3: Combine the buckets back together to maintain relative order
        return less_than + equal_to + greater_than