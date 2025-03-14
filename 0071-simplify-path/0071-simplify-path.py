class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        lst = path.split("/")
        for p in lst:
            if p == '' or p == '.':
                continue
            elif p == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(p)

        return "/" + "/".join(stack)