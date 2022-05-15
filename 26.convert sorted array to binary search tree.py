# Given an integer array nums where the elements are sorted in ascending order, 
# convert it to a height-balanced binary search tree.
# A height-balanced binary tree is
# a binary tree in which the depth of the two subtrees of every node never differs by more than one.

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 

    
def sortedArrayToBST(nums):
    if not nums:
        return None

    mid = (len(nums) - 1) // 2
    

    root = Node(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])


    return root

dat = []
def preOrder(node):
    
    if not node:
        return
     
    dat.append(node.val)
    preOrder(node.left)
    preOrder(node.right)

    return dat

# Test

root = sortedArrayToBST([1, 2, 3, 4, 5, 6, 7])
print(preOrder(root))
print(f''' 
       {preOrder(root)[0]}
    /     \    
   {preOrder(root)[1]}       {preOrder(root)[4]}
  / \     / \   
 {preOrder(root)[2]}   {preOrder(root)[3]}   {preOrder(root)[5]}   {preOrder(root)[6]} \n
___
''')
