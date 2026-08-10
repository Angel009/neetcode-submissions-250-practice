class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        simple_path = path.split("/")

        for place in simple_path:
            if place == "..":
                if stack:
                    stack.pop()
            elif place == "." or not place:
                continue
            
            else:
                stack.append(place)
        
        return "/" + "/".join(stack)