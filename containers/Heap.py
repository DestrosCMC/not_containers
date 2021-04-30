'''
This file implements the Heap data structure as a subclass of the BinaryTree.
The book implements Heaps using an *implicit*
tree with an *explicit* vector implementation,
so the code in the book is likely to be less helpful
than the code for the other data structures.
The book's implementation is the traditional implementation
because it has a faster constant factor
(but the same asymptotics).
This homework is using an explicit tree implementation to help
you get more practice with OOP-style programming and classes.
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
        Notice that in the BinaryTree class,
        we defined a __str__ function,
        but not a __repr__ function.
        Recall that the __repr__ function should return a
        string that can be used to recreate a valid instance of the class.
        Thus, if you create a variable using the command Heap([1,2,3])
        it's __repr__ will return "Heap([1,2,3])"

        For the Heap, type(self).__name__ will be the string "Heap",
        but for the AVLTree, this expression will be "AVLTree".
        Using this expression ensures that all subclasses of
        Heap will have a correct implementation of __repr__,
        and that they won't have to reimplement it.
        '''
        return type(self).__name__ + '(' + str(self.to_list('inorder')) + ')'

    def is_heap_satisfied(self):
        '''
        Whenever you implement a data structure,
        the first thing to do is to implement a function that checks whether
        the structure obeys all of its laws.
        This makes it possibleto automatically
        test whether insert/delete functions
        are actually working.
        '''
        if self.root:
            return Heap._is_heap_satisfied(self.root)
        return True

    @staticmethod
    def _is_heap_satisfied(node):
        '''
        FIXME:
        Implement this method.
        '''
        satisfied = True

        if not node:
            return True

        satisfied &= Heap._is_heap_satisfied(node.left)
        satisfied &= Heap._is_heap_satisfied(node.right)

        if not node.left:
            satisfied &= True

        else:
            satisfied &= (node.left.value >= node.value)

        if not node.right:
            satisfied &= True

        else:
            satisfied &= (node.right.value >= node.value)

        return satisfied

        '''
        left, right = True, True
        if not node:
            return True
        if node.left:
            left = node.value <= node.left.value and
            Heap._is_heap_satisfied(node.left)
        if node.right:
            right = node.value <= node.right.value and
            Heap._is_heap_satisfied(node.right)

        return left and right
        '''

    def insert(self, value):
        '''
        Inserts value into the heap.
        '''
        if self.root:
            nodess = self.__len__()
            route = "{0:b}".format(nodess + 1)[1:]
            self.root = Heap._insert(self.root, value, route)
        else:
            self.root = Node(value)

    @staticmethod
    def _insert(node, value, route):
        if route[0] == '0':
            if not node.left:
                node.left = Node(value)
            else:
                node.left = Heap._insert(node.left, value, route[1:])

        if route[0] == '1':
            if not node.right:
                node.right = Node(value)
            else:
                node.right = Heap._insert(node.right, value, route[1:])

        if route[0] == '0':
            if node.left.value < node.value:
                temp = node.value
                node.value = node.left.value
                node.left.value = temp
                return node
            else:
                return node

        if route[0] == '1':
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

        FIXME:
        Implement this function.
        '''
        for item in list(xs):
            self.insert(item)

    def find_smallest(self):
        '''
        Returns the smallest value in the tree.

        FIXME:
        Implement this function.
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
            self.root = Heap._trickle(self.root)

    @staticmethod
    def _remove_bottom_right(node, route):
        deleted = ""
        if len(route) == 0:
            return None, None
        if route[0] == '0':
            if len(route) == 1:
                deleted = node.left.value
                node.left = None
            else:
                deleted, node.left = Heap._remove_bottom_right(
                    node.left, route[1:])
        if route[0] == '1':
            if len(route) == 1:
                deleted = node.right.value
                node.right = None
            else:
                deleted, node.right = Heap._remove_bottom_right(
                    node.right, route[1:])
        return deleted, node

    @staticmethod
    def _trickle(node):
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
