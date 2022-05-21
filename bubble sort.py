class Sorting:
    def bubble(self, nums):

        outer = len(nums) - 1 # n - 1 = 4
        inner = len(nums) - 1 # n - 2 = 3
        idx = 0

        while idx <= outer:
            for i in range(inner):
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                else:
                    i += 1
            idx += 1
        return nums
                    




print(Sorting().bubble([1,2,3,4]))
print(Sorting().bubble([5,6,2,3,1]))
print(Sorting().bubble([5,8]))
print(Sorting().bubble([5,6,2,3]))
print(Sorting().bubble([5]))
print(Sorting().bubble([]))



