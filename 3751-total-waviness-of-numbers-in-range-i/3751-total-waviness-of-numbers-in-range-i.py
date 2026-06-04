class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        total_waviness = 0
        
        for num in range(num1, num2 + 1):
            # Numbers with fewer than 3 digits have a waviness of 0
            if num < 100:
                continue
                
            s = str(num)
            n = len(s)
            
            # Check every digit except the first and last
            for i in range(1, n - 1):
                # Peak condition
                if s[i] > s[i - 1] and s[i] > s[i + 1]:
                    total_waviness += 1
                # Valley condition
                elif s[i] < s[i - 1] and s[i] < s[i + 1]:
                    total_waviness += 1
                    
        return total_waviness