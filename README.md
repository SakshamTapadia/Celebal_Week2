# Simple Linked List Implementation
A clean, easy-to-understand Python implementation of a singly linked list using Object-Oriented Programming principles.

## What is a Linked List?
A linked list is like a chain of connected boxes, where each box contains:
- **Data** (the actual value you want to store)
- **A pointer** to the next box in the chain

Unlike arrays, linked lists don't store items in consecutive memory locations. Instead, each item "points" to the next one, creating a flexible chain that can grow or shrink as needed.

## Features

**Add items**
**Display** 
**Remove items** 
**Error handling** 
**Clean, readable code** 

### Available Methods
1. add(value)
2. show()
3. remove_at_position(pos) 

## Error Handling

The implementation gracefully handles common edge cases:
- **Empty list**
- **Invalid position**
- **Out of range**

## Code Structure

### Node Class
```python
class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 
```

### SimpleLinkedList Class
```python
class SimpleLinkedList:
    def __init__(self):
        self.first = None 
```

## Example Output
```
Creating a new linked list

Adding items to the list:
Added 10
Added 20
Added 30
Added 40
Added 50

========================================
List contents: 10 -> 20 -> 30 -> 40 -> 50

Let's try removing some items:

Removing item at position 3:
Removed '30' from position 3
List contents: 10 -> 20 -> 40 -> 50

Removing item at position 1:
Removed '10' from position 1
List contents: 20 -> 40 -> 50

Trying to remove item at position 10:
Position 10 doesn't exist in the list!
List contents: 20 -> 40 -> 50

Done!
```

## Technicalities Met

**OOP Implementation**: Uses classes and encapsulation  
**Node Management**: Proper node creation and linking  
**Add Functionality**: Appends items to the end  
**Display Functionality**: Shows list contents clearly  
**Delete by Position**: Removes items using 1-based indexing  
**Exception Handling**: Manages empty list and out-of-range scenarios  
**Sample Testing**: Includes comprehensive test cases  

## Getting Started

1. Copy the code into a Python file (e.g., `linked_list.py`)
2. Run the file: `python linked_list.py`
3. See the demonstration in action!
4. Modify the test cases to experiment with your own data
