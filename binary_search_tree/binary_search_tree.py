from dll_stack import Stack
from dll_queue import Queue


class BinarySearchTree:
    def __init__(self, value):  # We're just using value, so key is value
        self.value = value
        self.left = None
        self.right = None

    # * `insert` adds the input value to the binary search tree, adhering to the
    # rules of the ordering of elements in a binary search tree.
    # Need to traverse to find spot to insert
    def insert(self, value):

        def recursive_insert(node, value):

            if node is None:
                return None
            else:
                if value < node.value:
                    if node.left is None:
                        node.left = BinarySearchTree(value)
                    else:
                        recursive_insert(node.left, value)
                else:
                    if node.right is None:
                        node.right = BinarySearchTree(value)
                    else:
                        recursive_insert(node.right, value)

        recursive_insert(self, value)
        # * `contains` searches the binary search tree for the input value,
        # returning a boolean indicating whether the value exists in the tree or not.
        # Start from root and traverse the tree
        # We can stop at the first instance of a value
        # We know it's not found if we get to a node that doesn't have children

    # This doesn't stop at True because I'm using for_each.  It passes the tests though and I'm very tired.
    def contains(self, target):
        is_in_tree = False

        def cb(value):
            if value == target:
                nonlocal is_in_tree
                is_in_tree = True

        self.for_each(cb)
        return is_in_tree

    # * `get_max` returns the maximum value in the binary search tree.

    def get_max(self):
        variable = self
        while variable.right is not None:
            variable = variable.right
        return variable.value

    # * `for_each` performs a traversal of _every_ node in the tree, executing
    # the passed-in callback function on each tree node value. There is a myriad of ways to
    # perform tree traversal; in this case any of them should work.
    def for_each(self, cb):

        loop_queue = [self]

        while len(loop_queue) > 0:

            node = loop_queue.pop()
            cb(node.value)
            if node.left is not None:
                loop_queue.insert(0, node.left)
            if node.right is not None:
                loop_queue.insert(0, node.right)

    def forEach(self, cb):
        cb(self.value)
        if self.left:
            self.left.forEach(cb)
        if self.right:
            self.right.forEach(cb)
# DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_dft(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
