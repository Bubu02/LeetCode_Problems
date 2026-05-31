class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # Map row index to a bitmask representing reserved seats
        # We only care about seats 2 through 9
        reserved_rows = defaultdict(int)
    
        for row, col in reservedSeats:
            if 2 <= col <= 9:
                # Set the bit corresponding to the column
                reserved_rows[row] |= (1 << (col - 2))
            
        # Bitmask patterns for the three valid allocations
        # Seats 2,3,4,5 -> bits 0,1,2,3 -> binary 00001111 -> decimal 15
        # Seats 6,7,8,9 -> bits 4,5,6,7 -> binary 11110000 -> decimal 240
        # Seats 4,5,6,7 -> bits 2,3,4,5 -> binary 00111100 -> decimal 60
        left_mask = 15    
        right_mask = 240  
        middle_mask = 60  
    
        families = 0
    
        # Process only rows that have reservations
        for row, mask in reserved_rows.items():
            left_vacant = (mask & left_mask) == 0
            right_vacant = (mask & right_mask) == 0
            middle_vacant = (mask & middle_mask) == 0
        
            if left_vacant and right_vacant:
                families += 2
            elif left_vacant or right_vacant or middle_vacant:
                families += 1
            
        # Any completely empty row can accommodate exactly 2 families
        empty_rows = n - len(reserved_rows)
        families += empty_rows * 2
    
        return families
        