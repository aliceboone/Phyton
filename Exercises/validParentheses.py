'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false'''

def isValid(strs):
    stack = [] # "()"
    closeToOpen = {")" : "(", "]" : "[", "}" : "{"}

    for c in strs:
        if c in closeToOpen:
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False

print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))