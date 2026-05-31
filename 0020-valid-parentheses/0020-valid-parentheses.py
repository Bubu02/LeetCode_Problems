class Solution:
    def isValid(self, s: str) -> bool:
        paired = {')':'(', '}':'{',']':'['}
        answer = []
        for char in s:
            if char in paired.values():
                answer.append(char)
            elif char in paired:
                if answer:
                    if answer.pop() != paired[char]:
                        return False
                else:
                    return False
        return False if len(answer) > 0 else True
        