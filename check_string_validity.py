""" 
Given a string s contaning just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the smae type

"""

def check_string_validity(s):

    stack = []
    brackets = '{}()[]'
    brackets_obj = {'{':'}', '(':')', '[':']'}

    if len(s) < 2:
        return False
    for brac in [*s]:
        if brac in brackets:
            stack.append(brac)
        if brac in brackets_obj.values() and brac == brackets_obj.get(stack[stack.index(brac)-1]):
            stack = stack[:len(stack)-2]
        elif brac in brackets_obj.values() and brac != brackets_obj.get(stack[stack.index(brac)-1]):
            return False
        
    return True
   

# Test Check
print(check_string_validity('()')) # True
print(check_string_validity('()[]{}')) # True
print(check_string_validity('(]')) # False
print(check_string_validity('([{}])')) # True
print(check_string_validity('([)]')) # False
