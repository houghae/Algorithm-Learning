
class Node:
    """
    An object for storing a single node of a linked list.
    It models two attributes. Data and the link to the next node in the list.
    """
    data = None
    nextNode = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"Node data: {self.data}"

class SinglyLinkedList:
    """
    A linear data structure that stores values in nodes. 
    
    The list maintains a reference to the first node, head. 
    Each node points to the next node in the list.

    Attributes:
    head: The head node of the list.
    """

    def __init__(self):
        self.head = None
        # Maintain a count attribute to allow len() to be implemented in constant time.
        #self.count = 0

    def isEmpty(self):
        return self.head == None

    def size(self):
        """
        Return number of nodes in the list.

        Takes O(n), or linear, time.
        """
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.nextNode

        return count
    
    def add(self, data):    







#def main():
#if __name__=="__main__":
#    main()
