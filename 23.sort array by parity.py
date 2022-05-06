class Solution:

    # First Method
    def sortArrayByParity(self, nums):
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] % 2 == 0:
                left+=1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                if nums[left] % 2 != 0:
                    right -= 1
                else:
                    left += 1
                    right -= 1
        return nums

    # Pythonic Method # i line Code (^ Unbleivable ^_^)
    def sortArrayUsingsorted(self,nums):

        return sorted(nums, key=lambda x: x%2)




# Test
print(Solution().sortArrayByParity([3,2,1,5,6]))   
print(Solution().sortArrayByParity([2])) 
print(Solution().sortArrayByParity([3,1,2,4]))
print(Solution().sortArrayByParity([1,0,3])) 
print('==== Second Method===')
print(Solution().sortArrayUsingsorted([3,2,1,5,6]))   
print(Solution().sortArrayUsingsorted([2])) 
print(Solution().sortArrayUsingsorted([3,1,2,4]))
print(Solution().sortArrayUsingsorted([1,0,3])) 