class Solution:
    def isValid(self, s: str) -> bool:
        paired = {')':'(', '}':'{', ']':'['}
        opened = []
        for char in s:
            if char in paired.values():
                opened.append(char)
            elif char in paired:
                if opened:
                    if paired[char] != opened.pop():
                        return False
                else:
                    return False
        return True if len(opened) == 0 else False
        