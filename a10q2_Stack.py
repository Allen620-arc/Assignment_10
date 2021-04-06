"""
    Name: Allen Keettikkal
    NSID: alk423
    Student Number: 11278995
    Instructor: Jeffrey Long
"""

import Node as N


class Container(object):
    def __init__(self):
        self._size = 0  # how many elements in the stack

    def size(self):
        """
        Purpose
            returns the number of data values in the stack
        Return:
            The number of data values in the stack
        """
        return self._size

    def is_empty(self):
        """
        Purpose
            checks if the stack has no data in it
        Return:
            True if the stack has no data, or false otherwise
        """
        return self._size == 0


class Stack(Container):
    def __init__(self):
        Container.__init__(self)
        self.__top = None

    def push(self, value):
        """
        Purpose
            adds the given data value to the stack
        Pre-conditions:
            value: data to be added
        Post-condition:
            the value is added to the stack
        Return:
            (none)
        """
        new_node = N.Node(value, self.__top)
        self.__top = new_node
        self._size += 1

    def pop(self):
        """
        Purpose
            Removes and returns a data value from the stack.
            Note: the stack cannot be empty!
        Post-condition:
            the first value is removed from the stack
        Return:
            the first value in the stack, or None
        """
        assert not self.is_empty(), 'popped an empty stack'

        prev_first_node = self.__top
        result = prev_first_node.get_data()
        self.__top = prev_first_node.get_next()
        self._size -= 1
        return result

    def peek(self):
        """
        Purpose
            returns the value from the top of given stack
            without removing it
            Note: the stack cannot be empty!
        Post-condition:
            None
        Return:
            the value at the top of the stack
        """
        assert not self.is_empty(), 'peeked into an empty stack'

        first_node = self.__top
        result = first_node.get_data()
        return result
