
# Given an array of n integers nums, 
# a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k]
#  such that i < j < k and nums[i] < nums[k] < nums[j].

# Return true if there is a 132 pattern in nums, otherwise, return false.
import math
class Solution:
    '''
        i < j < k
        nums[i] < nums[k] < nums[j].
    '''

    # O(n^3) Sloution (not accepted from LeetCode)
    # def find132pattern(self, nums):
        
        # for i in range(len(nums)-2):
        #     for j in range(i+1, len(nums)-1):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] < nums[k] < nums[j]:
        #                 return True
        # return False

    def find132pattern(self, nums):
        
        first_num = math.inf
        for j in range(len(nums)-1):
            if first_num > nums[j]:
                first_num = nums[j]
            for k in range(j+1, len(nums)):
                if first_num < nums[k] < nums[j]:
                    return True
        return False
        




# Test
print(Solution().find132pattern([3,1,4,2]))  
print(Solution().find132pattern([-1,3,2,0])) 
print(Solution().find132pattern([1,2,3,4]))  


