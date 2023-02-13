# It enables us to execute documentation and embed interactive python sessions into the code and run/execute them
# for running doctest we use "doctest.testmod()"
# doctest.testfile("example.txt")
# the following below is the example of how doctest will execute
# read the text below to understand doctest

import doctest

class Stack():
    """ Basic stack implementation
        >>> stack = Stack()
        >>> stack.push(1)
        >>> stack.push(2)
        >>> stack.pop()
        2
        >>> stack.is_empty()
        False
        >>> stack.size()
        1
        """



    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return not bool(self.items)

    def size(self):
        return len(self.items)

    """
    Open Terminal or shortcut (Ctrl+Shift+~)
    type "python3" or "python" to open a session
    type "from basic_doctest import Stack" to import class Stack in this python session
    type "stack = Stack()"
    type "stack.push(1)" to test this method
    type "stack.push(2)" to append to this method
    type "stack.peek()" to test this method
    type "stack.pop()" to test this method
    type "stack.is_empty()" to test this method
    now copy from stack = Stack() till all test methods and paste it under class

    now running the stack as "python basic_doctest.py -v"

    """

if __name__ == '__main__':
    doctest.testmod()

""" 
testfile() : loos for files in the calling module directory
Any expected output must immediately follow the final '>>>" or "..." line containing the code and 
the expected output
if we use backslash in raw docstring then use print(f.__doc__) 
"""
