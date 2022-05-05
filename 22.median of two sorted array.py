# Given two sorted arrays nums1 and nums2 of size m and n respectively, 
# return the median of the two sorted arrays.

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # 1. Merga arrays
        mnums = nums1 + nums2

        # 2. sort arrays after merge (Selection Sort)
        for idx in range(len(mnums)):
            min_idx = idx
            for next_idx in range(idx+1, len(mnums)):
                if mnums[min_idx] > mnums[next_idx]:
                    min_idx = next_idx
            
            mnums[idx], mnums[min_idx] = mnums[min_idx], mnums[idx]

        # 3. Find Median
        median = 0
        mid_idx = len(mnums) // 2
        if len(mnums)%2 != 0:
            median = mnums[mid_idx]
        else:
            median = (mnums[mid_idx] + mnums[mid_idx-1]) / 2
            

        return mnums, median

# Test
print(Solution().findMedianSortedArrays([3,2,1],[5,6]))   # ([1, 2, 3, 5, 6], 3)
print(Solution().findMedianSortedArrays([2],[1])) # ([1, 2], 1.5)
print(Solution().findMedianSortedArrays([2,4,10],[1,3,9])) # ([1, 2, 3, 4, 9, 10], 3.5)

