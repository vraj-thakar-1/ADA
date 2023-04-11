"""
speaks following sequences and travel :)
inorder : LR*R
preorder : R*LR
postorder :LRR*

there are two properties left and right
"""

from node import Node

k=0
class BinaryTrre:
    def __init__(self, head: Node):
        self.head = head

    def add(self, new_node: Node):
        current_node = self.head
        while current_node:
            if new_node.value == current_node.value:
                raise ValueError("A node with that value already exists.")
            elif new_node.value < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = new_node  # link Node at left
                    break
            elif new_node.value > current_node.value:
                if current_node.right:
                    current_node = current_node.right  # link Node at right
                else:
                    current_node.right = new_node
                    break

    def find(self, value: int):
        global k
        k= 0
        self.inorder(value)
        if ( k == 2 ):
            k = 0
        else:
            print(f"tree does not have value:{value}")

    def inorder(self, value=None):  # great yarrrr
         self._inorder_recursive(self.head, value)
    def _inorder_recursive(self, current_node, value=None):

        if (value):
            if not current_node:
                return
            self._inorder_recursive(current_node.left, value)
            if value == current_node.value:
                print("your Node found: ", current_node)
                global k
                k = 2


            self._inorder_recursive(
                current_node.right, value
            )


        else:
            if not current_node:
                return
            self._inorder_recursive(current_node.left)

            print(current_node)
            self._inorder_recursive(
                current_node.right
            )

    def preorder(self):  # great yarrrr
        self._preorder_recursive(self.head)

    def _preorder_recursive(self, current_node):
        if not current_node:
            return
        print(current_node)
        self._preorder_recursive(current_node.left)

        self._preorder_recursive(
            current_node.right
        )

    def postorder(self):  # great yarrrr
        self._postorder_recursive(self.head)

    def _postorder_recursive(self, current_node):
        if not current_node:
            return

        self._postorder_recursive(current_node.left)

        self._postorder_recursive(
            current_node.right
        )
        print(current_node)
