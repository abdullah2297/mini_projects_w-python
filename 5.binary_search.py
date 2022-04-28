''' 
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums
If target exists, then return its index. Otherwise, return -1 
'''


## implementation of Binary Search

class Search:
    def binary_search(self, nums, target):
        left = 0
        right = len(nums) - 1
        
        if target in nums:
            while nums[left] <= nums[right]:
                mid = (left+right) // 2

                if nums[mid] == target:
                    return mid

                if target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        else:
            return -1
            
        return -1
 
 


# Test
print(Search().binary_search([ 2, 3, 4, 10, 40 ], 10)) # 3
print(Search().binary_search([ 2, 3, 4, 10, 40 ], 12)) # -1    # target not Exist
print(Search().binary_search([2], 2)) # 0
print(Search().binary_search([2], 3)) # -1    # target not Exist