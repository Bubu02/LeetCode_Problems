class Solution:
    def minOperations(self, n: int) -> int:
        operations = 0
        
        while n > 0:
            # If the last bit is 1, we must perform an operation
            if n & 1:
                operations += 1
                # Check if there are consecutive 1s (e.g., ending in binary 11)
                if (n & 3) == 3:
                    n += 1  # Add to carry over and clear consecutive 1s
                else:
                    n -= 1  # Subtract to clear the isolated 1
            
            # Shift right to inspect the next bit
            n >>= 1
            
        return operations