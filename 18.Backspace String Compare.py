
# Given two strings s and t, 
# return true if they are equal when both are typed into empty text editors. 
# '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.

class Solution:
    def backspaceCompare(self, s, t):
        def build(s):
            ans = []
            for c in s:
                if c != '#':
                    ans.append(c)
                else:
                    ans.pop()
            return "".join(ans)
        return build(s) == build(t)
        



print(Solution().backspaceCompare("ab#c",'ab#c'))
