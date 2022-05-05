class Solution:
    # Remove Element
    def removeElement(self, nums, val):
        left = 0
        right = len(nums)
        while left < right:
            if nums[left] == val:
                nums.pop(left)
                right-=1
            else:
                left+=1
        return len(nums), nums
    
    # Replace Element with placeholder
    def replaceElement(self, nums, val):
        left = 0
        right = len(nums)
        while left < right:
            if nums[left] == val:
                nums.pop(left)
                nums.append('_')
                left+=1
            else:
                left+=1
        return nums



print(Solution().removeElement([3,2,2,3],3))
print(Solution().removeElement([4,2,2,2],3))
print(Solution().removeElement([3],3))

print(Solution().replaceElement([3,2,2,3],3))
print(Solution().replaceElement([4,2,2,2],3))
print(Solution().replaceElement([3],3))