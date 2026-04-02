class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_num = 0
        curr_stack = ""

        for c in s:
            if c.isdigit():
                curr_num = (curr_num * 10) + int(c)

            elif c == "[":
                stack.append((curr_stack, curr_num))
                curr_num = 0
                curr_stack = ""
            elif c == "]":
                prev, num = stack.pop()
                curr_stack = prev + (curr_stack * num)
            else:
                curr_stack += c
        
        return curr_stack
        
        

        