class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        simple_path = path.split("/")

        for path in simple_path:
            if path == "..":
                if stack:
                    stack.pop()
            elif path == "." or not path:
                continue
            
            else:
                stack.append(path)
        
        return "/" + "/".join(stack)