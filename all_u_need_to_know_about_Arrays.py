# ==== What an Array is. ==== #
# Arrays are a simple data structure for storing lots of similar items.
# The items could be integers, strings, DVDs, games, books—anything really. 
# The items are stored in neighboring (contiguous) memory locations
# Every Element have index, and Value
# You can control your array through index


# === Create your First Array === #
arr1 = [2,4,6,7]
print(arr1)

# ==== Basic properties of Arrays. ==== #
# Access
print(arr1[0])

# Modify The Value
arr1[0] = 5
print(arr1)

# insertion
arr1.append(8)
print(arr1)

# delete element
arr1.pop()
print(arr1)

# Get length
print(len(arr1))

# Count Specified Value
print(arr1.count(4))

# Array Concatenation
arr2 = [8,9,10,11]
print(arr1+arr2)

# ==== Simple programming techniques with Arrays ===#
## Loop through array
for e in arr1:
    print( e*e )

# Check If The Item Exists In List
if 4 in arr1:
    print('yes')