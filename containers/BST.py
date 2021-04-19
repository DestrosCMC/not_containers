'''
This file implements the Binary Search Tree data structure.
The functions in this file are considerably
harder than the functions in the BinaryTree file.
'''

from containers.BinaryTree import BinaryTree, Node


class BST(BinaryTree):
    '''
    The BST is a superclass of BinaryTree.
    That means that the BST class "inherits"
    all of the methods from BinaryTree,
    and we don't have to reimplement them.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        If xs is a list (i.e. xs is not None),
        then each element of xs needs to be inserted into the BST.
        '''
        self.root = None
        if xs:
            self.insert_list(xs)

    def __repr__(self):
        '''
        Notice that in the BinaryTree class,
        we defined a __str__ function,
        but not a __repr__ function.
        Recall that the __repr__ function should return a string that
        can be used to recreate a valid instance of the class.
        Thus, if you create a variable using the command BST([1,2,3])
        it's __repr__ will return "BST([1,2,3])"

        For the BST, type(self).__name__ will be the string "BST",
        but for the AVLTree, this expression will be "AVLTree".
        Using this expression ensures that all subclasses
        of BST will have a correct implementation of __repr__,
        and that they won't have to reimplement it.
        '''
        return type(self).__name__ + '(' + str(self.to_list('inorder')) + ')'

    def __eq__(self, t2):
        '''
        This method checks to see if the contents of self and t2 are equal.
        The expression `a == b` desugars to `a.__eq__(b)`.

        NOTE:
        We only care about "semantic" equality,
        and not "syntactic" equality.
        That is, we do not care about the tree structure itself,
        and only care about the contents of what the tree contains.

        HINT:
        Convert the contents of both trees into a sorted list,
        then compare those sorted lists for equality.
        '''
        def list_elements(node):
            lst = []
            if not node.value:
                return lst
            lst = lst.append(node.value)
            if node.left:
                lst.append(list_elements(node.left))
            if node.right:
                lst.append(list_elements(node.right))
            return lst

        def flatten(lis):
            from collections.abc import Iterable
            for item in lis:
                if isinstance(item, Iterable) and not isinstance(item, str):
                    for x in flatten(item):
                        yield x
                else:
                    yield item
        a = list(flatten(list_elements(self)))
        b = list(flatten(list_elements(t2)))
        return sorted(a) == sorted(b)

    def is_bst_satisfied(self):
        '''
        Whenever you implement a data structure,
        the first thing to do is to implement a function that checks whether
        the structure obeys all of its laws.
        This makes it possible to automatically
        test whether insert/delete functions
        are actually working.
        '''
        if self.root:
            return BST._is_bst_satisfied(self.root)
        return True

    @staticmethod
    def _is_bst_satisfied(node):
        '''
        FIXME:
        Implement this method.
        '''
        left1, right1 = True, True

        if node.left:
            left1 = node.value > node.left.value and\
                BST._is_bst_satisfied(node.left)
        if node.right:
            right1 = node.value < node.right.value and\
                BST._is_bst_satisfied(node.right)

        return right1 and left1

    def insert(self, value):
        '''
        Inserts value into the BST.

        FIXME:
        Implement this function.

        HINT:
        Create a staticmethod helper function following
        the pattern of _is_bst_satisfied.
        '''
        if not self.root:
            self.root = Node(value)

        else:
            BST._insert(value, self.root)

    @staticmethod
    def _insert(value, node):
        if value < node.value:
            if not node.left:
                node.left = Node(value)
            else:
                BST._insert(value, node.left)

        elif value > node.value:
            if not node.right:
                node.right = Node(value)
            else:
                BST._insert(value, node.right)

        else:
            print("Unable to insert Value")

    def insert_list(self, xs):
        '''
        Given a list xs, insert each element of xs into self.

        FIXME:
        Implement this function.

        HINT:
        Repeatedly call the insert method.
        You cannot get this method to work correctly until
        you have gotten insert to work correctly.
        '''
        for item in xs:
            self.insert(item)

    def __contains__(self, value):
        '''
        Recall that `x in tree` desugars to `tree.__contains__(x)`.
        '''
        return self.find(value)

    def find(self, value):
        '''
        Returns whether value is contained in the BST.

        FIXME:
        Implement this function.
        '''
        if self.root:
            if BST._find(value, self.root):
                return True
        else:
            return False

    @staticmethod
    def _find(value, node):
        '''
        FIXME:
        Implement this function.
        '''
        if value == node.value:
            return True
        if value < node.value and node.left:
            return BST._find(value, node.left)
        if value > node.value and node.right:
            return BST._find(value, node.right)

    def find_smallest(self):
        '''
        Returns the smallest value in the tree.
        '''
        if self.root is None:
            raise ValueError('Nothing in tree')
        else:
            return BST._find_smallest(self.root)

    @staticmethod
    def _find_smallest(node):
        '''
        This is a helper function for find_smallest
        and not intended to be called directly by the user.
        '''
        if not node.left:
            return node.value
        else:
            return BST._find_smallest(node.left)

    def find_largest(self):
        '''
        Returns the largest value in the tree.

        FIXME:
        Implement this function.

        HINT:
        Follow the pattern of the _find_smallest function.
        '''
        if self.root:
            return BST._find_largest(self.root)
        else:
            return None

    @staticmethod
    def _find_largest(node):
        if not node.right:
            return node.value
        else:
            return BST._find_largest(node.right)

    def remove(self, value):
        '''
        Removes value from the BST.
        If value is not in the BST, it does nothing.

        FIXME:
        Implement this function.

        HINT:
        You should have everything else working before
        you implement this function.

        HINT:
        Use a recursive helper function.
        '''
        self.root = BST._remove(self.root, value)

    @staticmethod
    def _remove(node, value):
        if not node:
            return node

        if node.value > value:
            node.left = BST._remove(node.left, value)

        elif node.value < value:
            node.right = BST._remove(node.right, value)

        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left

            temp = node.right
            while temp.left:
                temp = temp.left

            node.value = temp.value
            node.right = BST._remove(node.right, node.value)

        return node

    def remove_list(self, xs):
        '''
        Given a list xs, remove each element of xs from self.

        FIXME:
        Implement this function.

        HINT:
        See the insert_list function.
        '''
        for item in xs:
            self.remove(item)
