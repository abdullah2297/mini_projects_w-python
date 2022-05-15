
#You are given a string s and an integer k,
# a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, 
# causing the left and the right side of the deleted substring to concatenate together.
# We repeatedly make k duplicate removals on s until we no longer can.
# Return the final string after all such duplicate removals have been made.
# It is guaranteed that the answer is unique.

class Solution:

    # def removeDuplicates(self, s, k):

    #     distinct = set(s)
    #     remove = []

    #     for char in distinct:
    #         remove.append(char*k)

    #     while True:
    #         found_dup = False

    #         for dup in remove:
    #             if dup in s:
    #                 s = s.replace(dup, '')
    #                 found_dup = True
    #         if found_dup == False:
    #             return s
    
    def removeDuplicates(self, s, k):
    
        stack = [['#',0]]
        for c in s:
            if stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c,1])
        
        distinct = ''.join(c*k for c,k in stack)
        return distinct





# Test
print(Solution().removeDuplicates("aaabbcccdd",3))  
print(Solution().removeDuplicates("pbbcs",2)) 
print(Solution().removeDuplicates("deeeedbbbcccbbddaa",4))  


