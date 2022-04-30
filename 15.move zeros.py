#Given an integer array nums, 
# move all 0's to the end of it while maintaining the relative order of the non-zero elements.

class Solution:
    # Memory = 15.5 MB
    # Runtime 171 ms
    def moveZeroes(self, nums):

        for i in range(len(nums))[::-1]:
            if nums[i] == 0:
                nums.append(nums.pop(i))
 
        return nums


    # Memory = 15.7 MB
    # Runtime 223 ms
    def moveZeroes2(self, nums):
    
        i = 0
        j = i + 1

        while j < len(nums):

            if nums[i] == 0 and nums[j] == 0: 
                j+=1
            elif nums[i] == 0 and nums[j] != 0: 
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
                j+=1
            elif nums[i] != 0 and nums[j] == 0: 
                i+=1
                j+=1
            elif nums[i] != 0 and nums[j] != 0:
                i += 1
                j += 1
        return nums











# Test
print("First Approch")
print(Solution().moveZeroes([0,1,0,0,3,0,5,0]))
print(Solution().moveZeroes([0,0,1]))
print("Second Approch")
print(Solution().moveZeroes2([0,1,0,0,3,0,5,0]))
print(Solution().moveZeroes2([0,0,1]))