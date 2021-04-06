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


class Queue(Container):
    def __init__(self):
        Container.__init__(self)
        self.__front = None  # the node chain starts here
        self.__back = None  # the node chain ends here

    def enqueue(self, value):
        """
        Purpose
            adds the given data value to the queue
        Pre-conditions:
            value: data to be added
        Post-condition:
            the value is added to the queue
        Return:
            (none)
        """
        new_node = N.Node(value, None)

        if self.is_empty():
            self.__front = new_node
            self.__back = new_node
        else:
            prev_last_node = self.__back
            prev_last_node.set_next(new_node)
            self.__back = new_node

        self._size += 1

    def dequeue(self):
        """
        Purpose
            removes and returns a data value from the queue
            Note: the queue cannot be empty!
        Post-condition:
            the first value is removed from the queue
        Return:
            the first value in the queue, or None
        """
        assert not self.is_empty(), 'dequeued an empty queue'

        prev_first_node = self.__front
        result = prev_first_node.get_data()
        self.__front = prev_first_node.get_next()
        self._size -= 1
        if self.size == 0:
            self.__back = None
        return result

    def peek(self):
        """
        Purpose
            returns the value from the front of queue
            without removing it
            Note: the queue cannot be empty!
        Post-condition:
            None
        Return:
            the value at the front of the queue
        """
        assert not self.is_empty(), 'peeked into an empty queue'

        first_node = self.__front
        result = first_node.get_data()
        return result