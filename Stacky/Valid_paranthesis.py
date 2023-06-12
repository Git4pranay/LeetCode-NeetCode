Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

# EASY

class Solution:
    def isValid(self, s):
        stack=['-']
        for i in range(len(s)):
            if s[i]=='(':
               stack.append('(')
            elif s[i]==')' and stack[-1]=='(':
                stack.pop()
            elif s[i]==')':
                stack.append(')')
            
            if s[i]=='[':
                stack.append('[')
            elif s[i]==']' and stack[-1]=='[':
                stack.pop()
            elif s[i]==']':
                stack.append(']')
            
            if s[i]=='{':
                stack.append('{')
            elif s[i]=='}' and stack[-1]=='{':
                stack.pop()
            elif s[i]=='}':
                stack.append('}')
        if stack[-1]=='-':
            return 1
        return 0
            
            

    
# BEATS 40%
O(n)