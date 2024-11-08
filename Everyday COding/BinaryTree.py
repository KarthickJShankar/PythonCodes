# class Node:
#     def _init_(self, val):
#         self.data = val
#         self.left = None
#         self.right = None
#
#
#
# class Solution:
# #Function to return a list containing the preorder traversal of the tree.
#     def preorder(self,root):
#         new_list = []
#         if not root:
#             return -1
#         current = root
#         while current.left:
#             current = current.left
#             new_list.append(current.values)

a = [1,2,3]
b = [1,3,2]
if a ==b:
    print('happy')
else:
    print('sad')