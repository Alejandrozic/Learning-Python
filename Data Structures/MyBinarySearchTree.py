from BinarySearchTree import BinarySearchTree

class MyBinarySearchTree(BinarySearchTree):

    def __init__(self):
        self.root = None

    def insert(self, data):
        # O(logN)
        if not self.root:
            self.root = Node(data)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if data < node.data:
            if node.left:
                self.insert_node(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right:
                self.insert_node(data, node.right)
            else:
                node.right = Node(data)

    def delete(self, data):
        # O(logN)
        if self.root:
            self.delete_node(data, self.root)

    def delete_node(self, data, node):
        if not node:
            return node

        if data < node.data:
            node.left = self.delete_node(data, node.left)

        elif data > node.data:
            node.right = self.delete_node(data, node.right)

        else:
            # Leaf
            if not node.left and node.right:
                del node
                return None

            # Single Right child
            if not node.left:
                tmp = node.right
                del node
                return tmp

            # Single Left child
            elif not node.right:
                tmp = node.left
                del node
                return tmp

            # Two Children
            predecessor = self.get_predecessor(node.left)
            node.data = predecessor.data
            node.left = self.delete_node(predecessor.data, node.left)

        return node

    def get_predecessor(self, node):
        if node.right:
            return self.get_predecessor(node.right)
        return node

    def find(self, data):
        # O(logN)
        pass

    def traverse(self):
        if self.root:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        if node.left:
            self.traverse_in_order(node.left)

        print '{0}'.format(node.data)

        if node.right:
            self.traverse_in_order(node.right)

    def get_min(self):
        if self.root:
            return self.get_min_recursion(self.root)

    def get_min_recursion(self, node):
        if node.left:
            return self.get_min_recursion(node.left)
        return node.data

    def get_max(self):
        if self.root:
            return self.get_max_recursion(self.root)

    def get_max_recursion(self, node):
        if node.right:
            return self.get_min_recursion(node.right)
        return node.data


class Node(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


if __name__ == '__main__':
    ###########
    # Testing #
    ###########

    bst = MyBinarySearchTree()

    # Test - with Integers
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(6)
    bst.insert(4)

    # Test - delete root
    bst.delete(10)

    # Test - get_min
    # Returns 4
    print bst.get_min()

    # Test - get_max
    # Returns 15
    print bst.get_max()

    # Test - In Order Traverse
    # 4, 5, 6, 15, None
    print bst.traverse()
