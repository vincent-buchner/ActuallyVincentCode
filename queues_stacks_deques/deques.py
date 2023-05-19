
# Give it name: Deque
class Deque:

    # This is what gets called when the deque is created
    def __init__(self):

        # The items in the deque
        self.__items = []

    # If you give me stuff at the front...
    def pushFront(self, stuff):

        # INSERT that stuff to the front of the deque
        self.__items.insert(0, stuff)

    # If you give me stuff at the back...
    def pushBack(self, stuff):

        # add stuff to the top of the deque
        self.__items.append(stuff)

    # See is the deque it empty
    def isEmpty(self):

        # Returns True if is empty
        # Returns False if not empty
        return self.__items == []

    # If you want less stuff on the front...
    def popFront(self):

        # Can't remove stuff that's not there
        if self.__items == []:
            return None
        
        # Otherwise...
        else:

            # pop the first item inserted off the queue
            return self.__items.pop(0)
        
    # If you want less stuff in the back...
    def popBack(self):

        # Can't remove stuff that's not there
        if self.__items == []:
            return None
        
        # Otherwise...
        else:

            # pop the first item inserted off the queue
            return self.__items.pop(len(self.__items) - 1)
    
    # See some stuff at the front... but don't get rid of it
    def peekFront(self):

        # See the the most recently added stuff
        return self.__items[0]
    
    # See some stuff at the back... but don't get rid of it
    def peekBack(self):

        # See the the most recently added stuff
        return self.__items[len(self.__items) - 1]
