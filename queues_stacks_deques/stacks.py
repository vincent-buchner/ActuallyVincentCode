
# Defines the name of the class; classes are used to make objects
class Stack:

    # This is what gets called when the stack is created
    def __init__(self):

        # The items in the stack
        self.__items = []

    # If you give me stuff...
    def push(self, stuff):

        # add stuff to the top of the stack
        self.__items.append(stuff)

    # See is the stack it empty
    def isEmpty(self):

        # Returns True if is empty
        # Returns False if not empty
        return self.__items == []

    # If you want less stuff...
    def pop(self):

        # Can't remove stuff that's not there
        if self.__items == []:
            return None
        
        # Otherwise...
        else:

            # pop the top item off the stack
            return self.__items.pop()
    
    # See some stuff... but don't get rid of it
    def peek(self):

        # See the the most recently added stuff
        return self.__items[len(self.__items) - 1]
    


