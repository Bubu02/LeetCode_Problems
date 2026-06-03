class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array to optimize binary search time complexity
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        
        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (m + n + 1) // 2 - partitionX
            
            # If partitionX is 0, nothing is on the left side of nums1. Use -infinity
            # If partitionX is m, nothing is on the right side of nums1. Use +infinity
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == m else nums1[partitionX]
            
            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == n else nums2[partitionY]
            
            # Check if we found the correct partition
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # If the total number of elements is odd
                if (m + n) % 2 == 1:
                    return float(max(maxLeftX, maxLeftY))
                # If the total number of elements is even
                else:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
            
            # We are too far right in nums1, move left
            elif maxLeftX > minRightY:
                high = partitionX - 1
            # We are too far left in nums1, move right
            else:
                low = partitionX + 1
                
        raise ValueError("Input arrays are not sorted.")