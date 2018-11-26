from BinarySearchTree import BinarySearchTree


class AVL(BinarySearchTree):

    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if not node:
            return Node(data)

        if data < node.data:
            node.left = self.insert_node(data, node.left)

        else:
            node.right = self.insert_node(data, node.right)

        node.height = max(self.calc_height(node.left) - self.calc_height(node.right)) + 1

        return self.violations(data, node)

    def violations(self, data, node):
        balance = self.calc_balance(node)

        # Doubly Left Heavy
        if balance > 1 and data < node.left.data:
            return self.rotate_right(node)

        # Doubly Right Heavy
        if balance < -1 and data > node.right.data:
            return self.rotate_left(node)

        # Left Right Heavy
        if balance > 1 and data > node.left.data:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Right Left Heavy
        if balance < -1 and data < node.right.data:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

    def calc_height(self, node):
        if not node:
            return -1

        return node.height

    def calc_balance(self, node):
        if not node:
            return 0

        return self.calc_height(node.left) - self.calc_height(node.right)

    def rotate_right(self, node):
        tmp_left = node.left
        tmp_right = tmp_left.right

        tmp_left.right = node
        node.left = tmp_right

        node.height = max(self.calc_height(node.left), self.calc_height(node.right)) + 1
        tmp_left.height = max(self.calc_height(tmp_left.left), self.calc_height(tmp_left.right)) + 1

        return tmp_left

    def rotate_left(self, node):
        tmp_right = node.right
        t = tmp_right.left

        tmp_right.left = node
        node.right = t

        node.height = max(self.calc_height(node.left), self.calc_height(node.right)) + 1
        tmp_right.height = max(self.calc_height(tmp_right.left), self.calc_height(tmp_right.right)) + 1

        return tmp_right

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

        if not node:
            return node

        node.height = max(self.calc_height(node.left) - self.calc_height(node.right)) + 1

        balance = self.calc_balance(node)

        # Doubly Left Heavy
        if balance > 1 and self.calc_balance(node.left) >= 0:
            return self.rotate_right(node)

        # Doubly Right Heavy
        if balance < -1 and self.calc_balance(node.right) <= 0:
            return self.rotate_left(node)

        # Left Right Heavy
        if balance > 1 and self.calc_balance(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Right Left Heavy
        if balance < -1 and self.calc_balance(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def get_predecessor(self, node):
        if node.right:
            return self.get_predecessor(node.right)
        return node

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
        self.height = 0
        self.left = None
        self.right = None
