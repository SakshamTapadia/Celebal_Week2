#Implement a Linked List in Python Using OOP and Delete the Nth Node
"""Create a Python program that implements a singly linked list using Object-Oriented Programming (OOP) principles. 
Your implementation should include the following: A Node class to represent each node in the list. 
A LinkedList class to manage the nodes, with methods to: 
Add a node to the end of the list 
Print the list 
Delete the nth node (where n is a 1-based index) 
Include exception handling to manage edge cases such as: Deleting a node from an empty list 
                                                         Deleting a node with an index out of range 
Test your implementation with at least one sample list.
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SimpleLinkedList:
    def __init__(self):
        self.first = None
    
    def add(self, value):
        new_item = Node(value)
        if not self.first:
            self.first = new_item
            return
        
        current = self.first
        while current.next:
            current = current.next
        current.next = new_item
    
    def show(self):
        if not self.first:
            print("The list is empty")
            return
        
        print("List contents:", end=" ")
        current = self.first
        items = []
        while current:
            items.append(str(current.value))
            current = current.next
        print(" -> ".join(items))
    
    def remove_at_position(self, position):
        if not self.first:
            print("Can't remove from an empty list!")
            return False
        if position < 1:
            print("Position must be 1 or higher!")
            return False
        
        if position == 1:
            removed_value = self.first.value
            self.first = self.first.next
            print(f"Removed '{removed_value}' from position 1")
            return True
        
        current = self.first
        for i in range(position - 2):
            if not current or not current.next:
                print(f"Position {position} doesn't exist in the list!")
                return False
            current = current.next
        
        if not current.next:
            print(f"Position {position} doesn't exist in the list!")
            return False
        
        removed_value = current.next.value
        current.next = current.next.next
        print(f"Removed '{removed_value}' from position {position}")
        return True


# Example usage
if __name__ == "__main__":
    print("Creating a new linked list")
    my_list = SimpleLinkedList()
    print("\nAdding items to the list:")
    items_to_add = [10, 20, 30, 40, 50]
    for item in items_to_add:
        my_list.add(item)
        print(f"Added {item}")
    
    print("\n" + "="*40)
    my_list.show()
    
    print("\nLet's try removing some items:")
    
    print(f"\nRemoving item at position 3:")
    my_list.remove_at_position(3)
    my_list.show()
    
    print(f"\nRemoving item at position 1:")
    my_list.remove_at_position(1)
    my_list.show()
    
    print(f"\nTrying to remove item at position 10:")
    my_list.remove_at_position(10)
    my_list.show()
    
    print("\nDone!")
