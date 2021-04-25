'''
This file implements the Heap data structure as a subclass of the BinaryTree.
The book implements Heaps using an *implicit* tree with an *explicit* vector
implementation, so the code in the book is likely to be less helpful than the
code for the other data structures. The book's implementation is the
traditional implementation because it has a faster constant factor (but the
same asymptotics). This homework is using an explicit tree implementation to
help you get more practice with OOP-style programming and classes.
'''

from containers.BinaryTree import BinaryTree, Node


class Heap(BinaryTree):
    '''
    FIXME:
    Heap is currently not a subclass of BinaryTree.
    You should make the necessary changes in the class declaration line above
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        If xs is a list (i.e. xs is not None),
        then each element of xs needs to be inserted into the Heap.
        '''
        super().__init__()
        if xs:
            self.insert_list(xs)

    def __repr__(self):
        '''
        Using this expression ensures that all subclasses of Heap will have a
        correct implementation of __repr__,
        '''
        return type(self).__name__ + '(' + str(self.to_list('inorder')) + ')'

    def is_heap_satisfied(self):
        '''
        function that checks whether
        the structure obeys all of its laws.
        '''
        if self.root:
            return Heap._is_heap_satisfied(self.root)
        return True

    @staticmethod
    def _is_heap_satisfied(node):
        '''
        Helper for is_heap_satisfied
        '''
        check = True
        if not node:
            return True
        check &= Heap._is_heap_satisfied(node.left)
        check &= Heap._is_heap_satisfied(node.right)

        if not node.left:
            check &= True
        else:
            check &= (node.left.value >= node.value)
        if not node.right:
            check &= True
        else:
            check &= (node.right.value >= node.value)

        return check

    def insert(self, value):
        '''
        Inserts value into the heap.
        '''
        if self.root:
            num_nodes = self.__len__()
            insert_path = "{0:b}".format(num_nodes + 1)[1:]
            self.root = Heap._insert(self.root, value, insert_path)
        else:
            self.root = Node(value)

    @staticmethod
    def _insert(node, value, insert_path):
        '''
        Helper function for insert
        '''
        # insert value
        if insert_path[0] == '0':
            if not node.left:
                node.left = Node(value)
            else:
                node.left = Heap._insert(node.left, value, insert_path[1:])
        if insert_path[0] == '1':
            if not node.right:
                node.right = Node(value)
            else:
                node.right = Heap._insert(node.right, value, insert_path[1:])
        # swap
        if insert_path[0] == '0':
            if node.left.value < node.value:
                temp = node.value
                node.value = node.left.value
                node.left.value = temp
                return node
            else:
                return node
        if insert_path[0] == '1':
            if node.right.value < node.value:
                temp = node.value
                node.value = node.right.value
                node.right.value = temp
                return node
            else:
                return node

    def insert_list(self, xs):
        '''
        Given a list xs, insert each element of xs into self.
        '''
        for value in list(xs):
            self.insert(value)

    def find_smallest(self):
        '''
        Returns the smallest value in the tree.
        '''
        return self.root.value

    def remove_min(self):
        '''
        Removes the minimum value from the Heap.
        If the heap is empty, it does nothing.
        '''
        if not self.root:
            pass
        else:
            num_nodes = self.__len__()
            remove_path = "{0:b}".format(num_nodes)[1:]
            last_val, self.root = Heap._remove_bottom_right(
                self.root, remove_path)
            if self.root:
                self.root.value = last_val
            print(str(self.root))
            self.root = Heap._trickle(self.root)

    @staticmethod
    def _remove_bottom_right(node, remove_path):
        '''
        Helper function to remove_min.
        Returns bottom right element in the tree as well as a modified tree
        with the bottom right node deleted.
        '''
        deleted_value = ""
        if len(remove_path) == 0:
            return None, None
        if remove_path[0] == '0':
            if len(remove_path) == 1:
                deleted_value = node.left.value
                node.left = None
            else:
                deleted_value, node.left = Heap._remove_bottom_right(
                    node.left, remove_path[1:])
        if remove_path[0] == '1':
            if len(remove_path) == 1:
                deleted_value = node.right.value
                node.right = None
            else:
                deleted_value, node.right = Heap._remove_bottom_right(
                    node.right, remove_path[1:])
        print(deleted_value, str(node))
        return deleted_value, node

    @staticmethod
    def _trickle(node):
        '''
        Helper function to remove_min.
        Swaps the root node with its smallest child until the heap
        property is satisfied. Returns the modified tree
        '''
        if Heap._is_heap_satisfied(node):
            pass
        else:
            if not node.left and node.right:
                temp = node.value
                node.value = node.right.value
                node.right.value = temp
                node.right = Heap._trickle(node.right)
            elif node.left and not node.right:
                temp = node.value
                node.value = node.left.value
                node.left.value = temp
                node.left = Heap._trickle(node.left)
            elif node.left.value >= node.right.value:
                temp = node.value
                node.value = node.right.value
                node.right.value = temp
                node.right = Heap._trickle(node.right)
            elif node.left.value <= node.right.value:
                temp = node.value
                node.value = node.left.value
                node.left.value = temp
                node.left = Heap._trickle(node.left)
            else:
                pass
        return node
