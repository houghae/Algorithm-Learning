class Node:
    """
    An object for storing a single node of a linked list.
    It models two attributes. Data and the link to the next node in the list.
    """

    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode # This is the pointer.

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
        self.__count = 0

    def isEmpty(self):
        """
        Determine if linked list is empty.

        Takes O(1) time.
        """
        
        return self.head == None
    
    def __len__(self):
        """
        Return length of linked list.

        Takes O(1), or constant, time.
        """

        return self.__count

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
        """
        Prepend new node with data to head of the list.

        Takes O(1) time.
        """

        self.head = Node(data, nextNode=self.head) # This is creating a new node instance, adding the pointer to the current head node, and then assigning the new node as the head of that list. 
        self.__count += 1

    def search(self, key):
        """
        Search for first node containing data matching 'key' argument.

        Return the node, or 'None' if not found.
        Takes O(n) time.
        """

        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.nextNode
        return None
    
    def __repr__(self):
        """
        Return string representation of the list.

        Takes O(n) time.
        """
        # Create an empty list.
        # Assign the head of a list instance to a local variable.
        # Begin while loop
            # If variable == head, append the list to say "Head is 'someData'"
            # Elif the nextNode is None, append the list "Tail is 'someData'"
            # Else - append the list with 'someData'
            # Assign the nextNode of the variable to the variable.
        # Return '->'.join(list)

        nodeList = []
        currentNode = self.head
        while currentNode:
            if currentNode == self.head:
                nodeList.append(f"Head is {currentNode.data}")
            elif currentNode.nextNode is None: # More Pythonic to us is instead of == when checking for the exact object None.
                nodeList.append(f"Tail is {currentNode.data}")
            else:
                nodeList.append(f"{currentNode.data}")
            currentNode = currentNode.nextNode
        return "->".join(nodeList)
    






#def main():
#if __name__=="__main__":
#    main()
