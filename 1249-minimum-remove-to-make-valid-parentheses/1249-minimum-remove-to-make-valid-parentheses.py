class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Convert string to a list because strings are immutable in Python
        s_list = list(s)
        stack = []  # To store the indices of '('
        
        for i, char in enumerate(s_list):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    # Found a matching pair, pop the '(' index from stack
                    stack.pop()
                else:
                    # No matching '(', so this ')' is invalid. Mark it for removal.
                    s_list[i] = ""
                    
        # Any indices left in the stack represent '(' that never found a closing ')'
        while stack:
            s_list[stack.pop()] = ""
            
        # Rejoin the list into a single string, skipping the removed characters
        return "".join(s_list)