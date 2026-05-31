class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # The stack will store pairs: [char, count]
        stack = []
        
        for char in s:
            # If the stack isn't empty and the current char matches the top of the stack
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
            else:
                # Otherwise, push a new character with a count of 1
                stack.append([char, 1])
            
            # FIX: Check and pop inside the loop as soon as count reaches k
            if stack[-1][1] == k:
                stack.pop()
                
        # Reconstruct the string from the remaining characters in the stack
        return "".join(char * count for char, count in stack)