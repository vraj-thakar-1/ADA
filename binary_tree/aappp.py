from node import Node

from binary_tree import BinaryTrre

tree = BinaryTrre(Node(5))
tree.add(Node(10))
tree.add(Node(1))
tree.add(Node(13))
tree.add(Node(7))


# print(tree.head)
# print(tree.head.left)
# print(tree.head.right)
# print(tree.head.right.right)
# print(tree.head.right.left)

tree.inorder()
print("-------")
# tree.preorder()
# print('-------')
# tree.postorder()
print("-------find values----")
tree.find(5)
tree.find(1)
tree.find(7)
tree.find(1)
tree.find(13)
tree.find(41)
tree.find(454545)


# thank you
