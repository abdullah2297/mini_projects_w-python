
'''
Given an array of integers nums sorted in non-decreasing order,
find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.  
'''

class Solution:
    def searchRange(self, nums, target):
       
        left_most = self.left_search(nums, target)
        right_most = self.right_search(nums, target)
        return [left_most, right_most]
    
    def left_search(self,nums,target):
        
        left = 0
        right = len(nums) - 1
        tarI = -1 

        while left <= right:
            pivot = (left+right) // 2

            if nums[pivot] > target:
                right = pivot - 1
            elif nums[pivot] < target:
                left = pivot + 1
            else:
                tarI = pivot
                right = pivot - 1
        return tarI


    def right_search(self,nums, target):
        left = 0
        right = len(nums) - 1
        tarI = -1

        while left <= right:
            pivot = (left+right)//2
            
            if nums[pivot] > target:
                right = pivot - 1
            elif nums[pivot] < target:
                left = pivot + 1
            else:
                tarI = pivot
                left = pivot + 1
        
        return tarI

# Test
print(Solution().searchRange([4,5,5,6,7],5)) # [1, 2]
print(Solution().searchRange([4,5,5,5,6,7],5)) # [1, 3]
print(Solution().searchRange([4,5,5,5,6,6,6],6)) # [4, 6]
print(Solution().searchRange([4,5,5,5,6,7],2)) # [-1, -1]
print(Solution().searchRange([5,5],5)) # [0,1]
print(Solution().searchRange([],5)) # [-1,-1]





