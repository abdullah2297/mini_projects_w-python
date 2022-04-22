# Data-structure-and-Algorithms
This project isn't for learning purpose, it is to share the most important notes for me during the learning process.

## SELECTION SORT

- Selection sort is a neat algorithm but it's not very fast.
- To find the item in the list u have to check each item in the list, this takes O(n) times and u have to do that n times so the time will be O(n*n)

```
## Find the smallest number in the list
def find_smallest(arr):
  ''' return the smallest item index '''
  smallest = arr[0]  
  smallest_index = 0
  for item in range(len(arr)):
    if arr[item] < smallest:
      smallest = arr[item]
      smallest_index = item
  return smallest_index

## apply the selection sort algorithm
def selection_sort(arr):
  ''' Sort the list of items '''
  newArr = []
  for item in range(len(arr)):
    smallest = find_smallest(arr)
    newArr.append(arr.pop(smallest))
  return newArr
  
print(selection_sort([5,7,5,4,8,3,9]))
```
## RECURSION
- Recursion is where a function call itself
- There is no performance benfit using Recursion
- Recursive function has to part:-
-   Recursive case ==> function call itself
-   Base case ==> function dosn't call self again
```
## use Recursion to do counter
def countdown(num):
  print(num)
  if num <= 0: ## base case
    print("Finish")
  else:     ## Recursive case
    countdown(num-1)

countdown(8)
```
## D&C
- D&C gives you a new way to think about solving problems
- When you get a new problem, you don’t have to be stumped. Instead, you can ask, “Can I solve this if I use divide and conquer?”

#### How it work ==> 
- Figure out a simplest case as a base case
- Figure out how to reduce your problem and get to the base case.

#### Q1:- Given a list of the numbers How to add all the numbers and get total.
#### First way to solve this problem

```
def find_sum(my_list):
  total = 0
  for num in my_list:
    total +=num
  return total

print(find_sum([6,2,4]))
```
#### Second way is using D&C concept
```
## This function will go through this steps ::-
# 1- 6 + sum(2,4)
# 2- 6 + 2 + sum(4)
# 3- 6 + 2 + 4 ## this is total 
def find_sum2(my_list):
  if my_list == []: ## base case
    return 0
  else:
    return my_list[0] + find_sum2(my_list[1:]) ## Recursive Case

print(find_sum2([6,2,4]))
```

#### Q2: Write a recursive function to count the number of items in a list.
```
def find_count(my_list):
  if my_list == []:  ## base case
    return 0
  else:
    return 1 + find_count(my_list[1:])

print(find_count([6,2,4]))
```
## Quicksort 
- it is sorting algorithm and much faster one
- This algorithm use D&C concept
- Quicksort is unique because its speed depends on the pivot you choose.
#### How it work ==>
- Figure out the base case which is the length of array is less than 2
- Choose ur pivot (any item in your list) , choose a random element as the pivot. The average runtime of quicksort is O(n log n)!
- figure out two sub-arrays, the first is array of all items are less than the pivot, the second is array of all items are greater than the pivot
- Repeat the pervious two steps with sub-arrays and so on
- when u reach to the base case, combine all this things together to get sorted list

#### Example
```
def qsort(my_list):
  if len(my_list) < 2: ## 1-base case
    return my_list
  else:
    pivot = my_list[0] ## 2-pivot
    less = [i for i in my_list[1:] if i <= pivot] ##3-first sub-array
    greater = [i for i in my_list[1:] if i > pivot] ##4-second sub-array
    return qsort(less) + [pivot] + qsort(greater) ## Recursive base

print(qsort([8,7,6]))
```
## Hash Tables 
- Hash function is a function where u put in a string input and u get back a number
- Python has hash tables they are called dictinaries
- Hash tables are fast in insertation, deletion and search
- When to use hash tables =>
- 1- when u want to mapping data to values
- 2- Checking for duplicates is very fast with a hash table.
- 3- using a hash tables as a cache

#### Examples.
#### 1- Suppose you’re running a voting booth. Naturally, every person can vote just once

```
voted = {} ## dictinary is a hash table
voted['abdu'] = False
def check_voter(name):
  if voted.get(name): ## return true or false
    print(f"sorry {name} u had been voted")
  else:
    voted[name] = True
    print(f"Let {name} voted")

check_voter("Ahmed")
check_voter("Ali")
check_voter("Ahmed")
check_voter("abdu")
print(voted)
```
#### collision:- two keys have been assigned the same slot.
#### There are many different ways to deal with collisions. The simplest one is this: if multiple keys map to the same slot, start a linked list at that slot.
#### To avoid collisions, you need:
- A low load factor
- A good hash function

## Breadth-first search 
- Graphs are a way to model how different things are connected to one another.
- Graphs are made up of nodes and edges. A node can be directly connected to many other nodes. Those nodes are called its neighbors.
- breadth-first search is algorithm to solve a shortest-path problem.
- breadth-first can help answer two types of questions:
- • Question type 1: Is there a path from node A to node B?
- • Question type 2: What is the shortest path from node A to node B?

# Questions
### Q1: Write a Python program for binary search.
```
def binary_search(lis,item):
  '''Search for item in list with binary search'''
  ## determine first and last index
  first = 0
  last = len(lis)-1
  found = False
  ## loop in the 
  while( first<=last and not found):
    mid = (first + last)//2
    if lis[mid] == item:
      found = True
      print(f"index of item is: { lis.index(item)}")
    else:
      if item < lis[mid]:
        last = mid - 1
      else:
        first = mid + 1

  return found

print(binary_search([1,2,3,5,8], 2))  # True
print(binary_search([1,2,3,5,8], 10)) # false
```

### Q2: Write a Python program for sequential search ###
```
def linear_search(lis, item):
  ''' search for item in list using seq search'''
  pos = 0
  found = False
  while (pos < len(lis) and not found):
    if item == lis[pos]:
      found = True
    else:
      pos +=1

  return found

print(linear_search([1,2,3],3))  # True
print(linear_search([1,2,3],5))  # False
```
### Q3: Write a Python program to sort a list of elements using the selection sort algorithm. ##

```
def selection_sort(lis):

  for slot in range(len(lis)):
    min_idx = slot

    for location in range(slot+1, len(lis)):

      if lis[min_idx] > lis[location]:
        min_idx = location
  
    lis[slot], lis[min_idx] = lis[min_idx], lis[slot]
  return lis


print(selection_sort([1,2,50,15,5,4,0]))
```
### Q4: Write a Python program to locate the left insertion point for a specified value in sorted order.
```
import bisect
def insertation_index(lis, item):
  lis.sort() ## sort your list O(n log n)
  insert_point = bisect.bisect_left(lis,item)
  return insert_point

family_ages = [18,22,24,45,64]
print(f"insertation_index for dad age: {insertation_index(family_ages,58)}")
```
#### Notes : Time complexity for bisec_left is O(log n), it is use Binary search

### Q5: Write a Python program to insert items into a list in sorted order.
```
def insert_item(lis, item):
  lis.sort()
  bisect.insort(lis, item)
  return lis

print(f" New list : {insert_item(family_ages,58)}")
```
#### Notes : The time complexity of insort() is O(n)

### Q6: Write a Python program to create a queue and display all the members and size of the queue.

```
from queue import Queue
# initialize New Queue
my_queue = Queue()
# Check for size
print(f"Queu size : {my_queue.qsize()}")
# Add some data
my_queue.put('Ahmed')
my_queue.put('Abdullah')
my_queue.put('Ali')
# Check size again
print(f"Queu size after adding data : {my_queue.qsize()}")
# get some data
print(f"first get : {my_queue.get()}")
print(f"second get : {my_queue.get()}")
print(f"Third get  : {my_queue.get()}")


print(f"is a queue become empty? : {my_queue.empty()}")
```
#### Notes:
- Time Complexity : O(1)
- List is a Python’s built-in data structure that can be used as a queue but it requring o(n) time in insertation and deletion


### Q7: Write a Python program to create a Stack and display all the members and size of the stack.
```
from queue import LifoQueue
# initialize New Stack
my_stack = LifoQueue()
# Check for size
print(f"stack size : {my_stack.qsize()}")
# Add some data
my_stack.put('Ahmed')
my_stack.put('Abdullah')
my_stack.put('Ali')
# Check size again
print(f"stack size after adding data : {my_stack.qsize()}")
# get some data
print(f"first get : {my_stack.get()}")
print(f"second get : {my_stack.get()}")
print(f"Third get  : {my_stack.get()}")

print(f"is a stack become empty? : {my_stack.empty()}")
```
