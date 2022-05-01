
# Given a string s, 
# reverse the order of characters in each word within a sentence 
# while still preserving whitespace and initial word order.

class Solution:
    def reverseWords(self, s):

        lis = s.split(' ')
        reversed_lis = []
        reversed_str = " "
        
        for letter in lis:
            letter = letter[::-1]
            reversed_lis.append(letter)
        
        reversed_str = reversed_str.join(reversed_lis)

        return reversed_str



# Test
print(Solution().reverseWords("Let's take LeetCode contest"))
print(Solution().reverseWords("Hello Pythonista"))