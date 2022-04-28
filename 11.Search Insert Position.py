'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
'''

class Solution:

    ## LinearSearch O(n)
    def linear_search(self, nums, target):

        if target in nums:
            return nums.index(target)
        else:
            for i in range(len(nums)):
                if nums[i] < target:
                    i+=1
                elif nums[i] > target:
                    return nums.index(nums[i])

    # Binary Search O(n log n)
    def binary_search(self, nums, target):
            
            left = 0
            right = len(nums) - 1

            while left <= right:
                
                pivot = (left+right) // 2

                if nums[pivot] == target:
                    return pivot

                if target < nums[pivot]:
                    right = pivot - 1

                elif target > nums[pivot]:
                    left = pivot + 1

            return left






# Test
# Linear Search
print("Linear Search")
print(Solution().linear_search([1,3,5,6],5))
print(Solution().linear_search([1,3,5,6],2))
print(Solution().linear_search([1,3,5,6,8],7))

# Binary Search
print("Binary Search")
print(Solution().binary_search([1,3,5,6],5))
print(Solution().binary_search([1,3,5,6],2))
print(Solution().binary_search([1,3,5,6,8],7))