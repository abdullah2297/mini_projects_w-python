class Solution:
    def reverseString1(self, s):
        reversed_string = s[::-1]
        return reversed_string

    # Runtime: 223 ms
    # Memory Usage: 18.4 MB
    def reverseString2(self,s):
        i = 0
        j = len(s)-1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return s




# Test
print('Silicing Approach')
print(Solution().reverseString1(["h","e","l","l","o"]))
print('Two Pointer')
print(Solution().reverseString2(["h","e","l","l","o"]))
