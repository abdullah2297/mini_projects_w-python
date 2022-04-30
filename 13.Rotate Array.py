class Solution:
    def rotate(self, nums, k):

        for _ in range(k % len(nums)):
            nums.insert(0,nums.pop())
        return nums





#Test
print(Solution().rotate([1,2,3,4,5,6,7],3))