# Implementation of data structures (done by myself).

# STACK
class Stack:
    def __init__(self):
        '''Initialise the stack, and a variable that holds the index of the top of the stack.'''

        self._stack = []
        self._top = None

    def push(self, item):
        '''Push the given item to the top of the stack, while incrementing the pointer.'''

        self._stack.append(item)
        self._top = len(self._stack) - 1

    def pop(self):
        '''Remove the top item from the stack if not empty, and decrement the pointer.
        If the stack is empty, set the pointer to None.
        '''

        if not self.is_empty():
            self._stack.pop()
            if self.is_empty():
                self._top = None
            else:
                self._top = len(self._stack) - 1

    def peek(self):
        '''Return the item at the top of the stack; return False if stack is empty.'''

        if not self.is_empty():
            return self._stack[self._top]
        return False

    def is_empty(self):
        '''Return True if the stack is empty, and False if it is not.'''

        return not len(self._stack)

    @property
    def stack(self):
        '''Return the actual stack.'''

        return self._stack

    def size(self):
        '''Return the number of items in the stack.'''

        return len(self._stack)