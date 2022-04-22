# Searching in data structure refers to the process of finding the required information from a collection of items stored as elements in the computer memory.
### Linear Search
# The linear search algorithm iteratively searches all elements of the array.
# When the given data is unsorted, a linear search algorithm is preferred over other search algorithms.
# Do not need the sorted list of element
# Preferred for a small size data set
# Space complexity is O(n) Worest Case Time O(n)

## Binary Search
# Search the position of the searched element by finding the middle element of the array
# Need the sorted list of elements
# Preferred for a large size data set
# The worst-case complexity in binary search is O(n log n).


class Searching_algorithms:

    # Initialization Function
    def __init__(self, lis, x):
        self.lis = lis
        self.x = x

    # Sort Data For Binary Search # Unused in this Example
    def sort_data(self):
        self.lis.sort()
        return self.lis

    # Linear Search 
    def linear_search(self):
        
        if self.x in self.lis:
            for i in range(len(self.lis)):

                if self.lis[i] != self.x:
                    i+=1
                else:
                    return f"Using LinearSearch The Value you searching '{self.x}' at index {i}"
        else:
            return f"The value {self.x} not in the list"


    # Binary Search
    def binary_search_sorted(self):
        low = 0
        high = len(self.lis) - 1
        while high >= low:
            mid = (low + high) // 2
            if self.x == self.lis[mid]:
                return f"Using BinarySearch The Value you searching '{self.x}' at index {mid}"
            elif self.lis[mid] > self.x:
                high = mid - 1
            elif self.lis[mid] < self.x:
                low = mid + 1


# List for Test
my_lis = [1,2,3,4,5]

# Test1 Linear Search
data = Searching_algorithms(my_lis,4)
print(data.linear_search())

print("=========================")

## Test2 Binary Search
data3 = Searching_algorithms(my_lis,4)
print(data3.binary_search_sorted())
print("=========================")