# ============== PYTHON LISTS COMPREHENSIVE GUIDE ==============

# ✅ 1) List Basics
# Lists are ordered, mutable collections that can store heterogeneous data types
names = ["Bhanu", "Sandeep", "Abhay", "Devansh"]
print("Names List:", names)
print("Length of list:", len(names))  # Get number of items

# ✅ 2) Indexing in List
# Python uses 0-based indexing
print("\n=== Indexing ===")
print("Index 0 (First element):", names[0])
print("Index 1 (Second element):", names[1])

# ✅ 3) Negative Indexing
# Accesses elements from the end of the list
print("\n=== Negative Indexing ===")
print("Last item (-1):", names[-1])
print("Second last item (-2):", names[-2])

# ✅ 4) List Creation Methods
print("\n=== List Creation ===")
# Empty list
empty_list = []
print("Empty list:", empty_list)

# List with range
numbers = list(range(1, 8))  # [1, 2, 3, 4, 5, 6, 7]
print("Numbers from range:", numbers)

# List comprehension
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
print("Squares using comprehension:", squares)

# ✅ 5) Slicing
# Syntax: list[start:stop:step] (stop index is exclusive)
print("\n=== Slicing Operations ===")
print("Original list:", numbers)
print("Index 1 to 3 (exclusive):", numbers[1:3])  # [2, 3]
print("First 3 items:", numbers[:3])  # [1, 2, 3]
print("From index 4 to end:", numbers[4:])  # [5, 6, 7]
print("Every second item:", numbers[::2])  # [1, 3, 5, 7]
print("Reverse list:", numbers[::-1])  # [7, 6, 5, 4, 3, 2, 1]

# ✅ 6) List Operations
print("\n=== List Operations ===")
# Concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print("Concatenated lists:", combined)

# Repetition
repeated = list1 * 3
print("Repeated list:", repeated)

# Membership testing
print("Is 2 in list?", 2 in list1)  # True
print("Is 7 in list?", 7 in list1)  # False

# ✅ 7) List Methods
print("\n=== List Methods ===")
my_list = [1, 2, 3, 5, 6, 3, 2, 1, 4, 2, 5, 2, 4, 2, 1]

# Adding elements
my_list.append(12)  # Add to end
print("After append(12):", my_list)

my_list.insert(1, 15)  # Insert at specific position
print("After insert(1, 15):", my_list)

my_list.extend([20, 21, 22])  # Add multiple items
print("After extend():", my_list)

# Removing elements
popped = my_list.pop()  # Remove and return last item
print(f"After pop(): {my_list}, popped value: {popped}")

popped = my_list.pop(3)  # Remove at specific index
print(f"After pop(3): {my_list}, popped value: {popped}")

my_list.remove(2)  # Remove first occurrence of value
print("After remove(2):", my_list)

# Other operations
my_list.reverse()
print("After reverse():", my_list)

my_list.sort()
print("After sort():", my_list)

print("Count of 2:", my_list.count(2))  # Count occurrences
print("Index of 5:", my_list.index(5))  # Find first index

# ✅ 8) List Copying
print("\n=== List Copying ===")
original = [1, 2, 3]
shallow_copy = original.copy()  # or original[:]
deep_copy = original[:]  # Shallow copy for simple lists

original[0] = 99
print("Original:", original)  # [99, 2, 3]
print("Shallow copy:", shallow_copy)  # [1, 2, 3]

# For nested lists, use copy.deepcopy()
import copy
nested = [[1, 2], [3, 4]]
deep_nested = copy.deepcopy(nested)

# ✅ 9) List as Stack and Queue
print("\n=== List as Data Structures ===")
# Stack (LIFO)
stack = []
stack.append(1)  # push
stack.append(2)
stack.append(3)
print("Stack:", stack)
print("Pop from stack:", stack.pop())  # 3

# Queue (FIFO) - collections.deque is more efficient
from collections import deque
queue = deque([1, 2, 3])
queue.append(4)
print("Queue:", queue)
print("Pop from queue:", queue.popleft())  # 1

# ✅ 10) Advanced List Techniques
print("\n=== Advanced Techniques ===")
# Filtering
numbers = [1, 2, 3, 4, 5, 6]
evens = [x for x in numbers if x % 2 == 0]
print("Even numbers:", evens)

# Mapping
squared = [x**2 for x in numbers]
print("Squared numbers:", squared)

# Zipping lists
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
combined = list(zip(names, scores))
print("Zipped list:", combined)

# Unpacking
first, *middle, last = numbers
print(f"Unpacked: first={first}, middle={middle}, last={last}")

# ✅ 11) Performance Considerations
# - append() and pop() are O(1)
# - insert() and remove() are O(n)
# - Preallocate large lists when possible: [None] * size
# - Consider deque for frequent insertions/deletions at both ends

# ✅ 12) Common Pitfalls
# - Modifying list while iterating (create copy instead)
# - Assuming list.copy() creates deep copy for nested lists
# - Confusing list methods that modify vs. return new list