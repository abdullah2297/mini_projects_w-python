
############# First and Simple Method #############
# Node Contains :-
# Value,  next
# '3' ==> '5' == '7'

# This Class create separate Nodes
# class Node:
#     def __init__(self, data, next = None):
#         self.data = data
#         self.next = next

# # Create Nodes
# node1 = Node('3')
# node2 = Node('5')
# node3 = Node('7')

# # Connect Nodes
# node1.next = node2
# node2.next = node3

# curr = node1
# while True:
#     print(curr.data)
#     if curr.next is None:
#         break
#     curr = curr.next

############# Second and Dynamic Method #############

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        node = Node(value)   # Create Nodes
        if self.head is None:  # Check if you have a head or not
            self.head = node   # Assign current node to be a head
            return
        current_node = self.head
        while True:
            if current_node.next is None:
                current_node.next = node
                break
            current_node = current_node.next

    def printl(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

            
ll = Linkedlist()
ll.insert('3')
ll.insert('5')
ll.insert('7')
ll.printl()


