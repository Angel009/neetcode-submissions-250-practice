class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"(":")", "{":"}", "[":"]"}
        open_brackets = []

        for c in s:
            if c in brackets:
                open_brackets.append(c)
            else:
                if len(open_brackets) >= 1:
                    curr = open_brackets.pop()

                    if brackets[curr] != c:
                        return False
                else:
                    return False
        
        return len(open_brackets) == 0