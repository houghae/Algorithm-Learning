class Node:
    """
    An object for storing a single node of a linked list.
    It models two attributes. Data and the link to the next node in the list.
    """

    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode  # This is the pointer.

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
        self.__count = 0  # Maintain a count attribute to allow len() to be implemented in constant time.


    def isEmpty(self):
        """
        Determine if linked list is empty.

        Takes O(1) time.
        """
        
        return self.head == None
    
    def __len__(self):  # Special dunder method to allow use of len() on instances of these lists.
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
        Search for first node containing data matching the key.

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
        return " -> ".join(nodeList)
    
    def insert(self, data, index):
        """
        Insert new node at specified index position. 

        Insertion takes O(1) time, but finding the insertion point takes O(n) time due to traversing every node.
        Overall insert takes O(n) time. 
        """

        if index >= self.__count:
            raise IndexError("Index out of range")
        if index == 0:
            self.add(data)
        if index > 0:
            insertionNode = Node(data)
            position = index
            current = self.head
            while position > 1:
                current = current.nextNode
                position -= 1
            previousNode = current
            nextNode = current.nextNode
            previousNode.nextNode = insertionNode
            insertionNode.nextNode = nextNode
        self.__count += 1

    def removeWithKey(self, key):
        """
        Remove node containing data that matches the key. 

        Return the node, or None if key is not present in list.
        Takes O(n) time.
        """

        # Search along list until key is found. CAN NOT use the search method because it would return the node without the reference to the previous node. The search method would only work for a doubly linked list, not singly linked list.
        # If key is not found, return 'key not found' error.

        current = self.head
        found = False
        previous = None

        while current and not found:
            # Three cases could exist.
                # The key is found in current, which is also the head node.
                    # Change found to True, assign next node to head, decrement count by 1.
                # The key is found in current, which is NOT the head node.
                    # Change found to True, assign next node to current, assign decrement count by 1. 
                    # In order to preserve the link from the previous node, you can't just assign to current. It has to be the previous node's next node.
                # The key isn't found.
                    # Assign next node to current and repeat while loop. Decrement count by 1.
            if current.data == key and current is self.head:
                found = True
                self.head = current.nextNode
                self.__count -= 1
                return current
            elif current.data == key:
                found = True
                previous.nextNode = current.nextNode
                self.__count -= 1
                return current
            else:
                previous = current
                current = current.nextNode
        raise Exception("Key not found") # Could also just return None.



    def removeWithIndex(self, index):
        """
        Remove node at given index value.

        Takes O(n) time.
        """

        # Define current as head node, position as index.
        # If index is >= self.__count raise index error.
        # If index is 0, set head to next node.
        # While position is > 1:
            # Set current to next node
            # Decrement position by 1 

        current = self.head
        position = index

        if index >= self.__count:
            raise IndexError("Index out of range")
        if index == 0:
            self.head = current.nextNode
            self.__count -= 1
            return current
        while position > 1:
            current = current.nextNode
            position -= 1
        
        prevNode = current  # This removes the first pointer.
        current = current.nextNode
        nextNode = current.nextNode
        prevNode.nextNode = nextNode  # This creates a new pointer that bypasses current.
        self.__count -= 1
        return current  # Because the removed node is still assigned to current.

    def nodeAtIndex(self, index):
        """
        Return the node at a given index value.
        
        Takes O(n) time.
        """

        # This should be similar to insert method.

        current = self.head
        position = 0

        if index >= self.__count:
            raise IndexError("Index out of range")
        if index == 0:
            return current
        while position < index:
            current = current.nextNode
            position += 1
        return current
    
    def __iter__(self):
        current = self.head
        while current:
            yield current  # Yield returns a value while pausing a method and saving it's state. This can return values that would otherwise bog down memory.
            current = current.nextNode
        








#def main():
#if __name__=="__main__":
#    main()
