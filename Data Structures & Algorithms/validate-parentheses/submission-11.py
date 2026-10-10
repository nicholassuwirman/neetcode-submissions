#         i
# s = "([{}])"
# list = "([{"
# ([{

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if s[i] in "([{":
                stack.append(s[i])
            elif stack and s[i] == "}" and stack[-1] == "{":
                stack.pop()
            elif stack and s[i] == "]" and stack[-1] == "[":
                stack.pop()
            elif stack and s[i] == ")" and stack[-1] == "(":
                stack.pop() 
            else:
                return False

        if len(stack) == 0:
            return True
        else:
            return False

