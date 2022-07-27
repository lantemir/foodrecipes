#  ортировку вставкой 

arr = [9, -4, 6, 1, 7 ]
arrLength = len(arr)

for i in range(1, arrLength):
    for j in range(i, 0, -1):
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else:
            break

print (arr)






# class Stack:
#     def __init__(self, intial = None):
        
#         if isinstance(intial, list):
#             self.stack = intial
#         else:
#             raise TypeError
    
#     def add(self, item):
#         self.stack.append(item)
#         return self.stack

#     def remove(self):
#         itemrem = self.stack[-1]
#         self.stack = self.stack[0:-1:1]
#         return itemrem


# stack1 = Stack([5,3])

# print(stack1.stack)
# print( stack1.add(9))
# print( stack1.remove())
# print( stack1.remove())
# print(stack1.stack)





# # дерево

# class Node:
#     def __init__(self, data):

#         self.left = None
#         self.right = None
#         self.data = data

#     def insert(self, data):
# # Compare the new value with the parent node
#         if self.data:
#             if data < self.data:
#                 if self.left is None:
#                     self.left = Node(data)
#                 else:
#                     self.left.insert(data)
#             elif data > self.data:
#                 if self.right is None:
#                     self.right = Node(data)
#                 else:
#                     self.right.insert(data)
#         else:
#             self.data = data

# # Print the tree
#     def PrintTree(self):
#         if self.left:
#             self.left.PrintTree()
#         print( self.data),
#         if self.right:
#             self.right.PrintTree()

# # Use the insert method to add nodes
# root = Node(12)
# root.insert(6)
# root.insert(14)
# root.insert(3)
# root.PrintTree()



