# Given an integer array nums sorted in non-decreasing order, 
# return an array of the squares of each number sorted in non-decreasing order.

class Solution:
    def sortedSquares(self, nums):
        idx = 0
        limit = len(nums) - 1
        sq_nums = []
        while idx <= limit:
            sq_nums.append(nums[idx]**2)
            idx+=1
        
        sq_nums_sorted = sorted(sq_nums)
        return sq_nums_sorted

#Tese
print(Solution().sortedSquares([-2,0,1,2,5]))