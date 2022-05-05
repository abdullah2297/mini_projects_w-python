# Given an integer array nums sorted in non-decreasing order, 
# remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same.
# Do not allocate extra space for another array. 

class Solution:
    def removeDuplicates(self, nums):

        unique = 1
        i = 0
        ran = len(nums)-1
        while i < ran:
            if nums[i] != nums[i+1]:
                unique+=1
                i+=1
            else:
                nums.pop(i)
                ran -= 1

        return unique, nums
        
print(Solution().removeDuplicates([1,1,2,2,2,3,3,4,5]))
print(Solution().removeDuplicates([1,1]))
print(Solution().removeDuplicates([1]))
print(Solution().removeDuplicates([-1,0,0,0,0,3,3]))




