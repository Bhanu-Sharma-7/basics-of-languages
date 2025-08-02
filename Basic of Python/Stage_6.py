# ============== PYTHON LOOPS COMPREHENSIVE GUIDE ==============

# ✅ 1) For Loop Basics
print("=== Basic For Loop ===")
# range(10) generates numbers from 0 to 9 (10 is exclusive)
for i in range(10):
    print(i, end=' ')  # end=' ' keeps output on same line
# Output: 0 1 2 3 4 5 6 7 8 9

print("\n\n=== For Loop with range parameters ===")
# range(start, stop, step)
for i in range(2, 11, 2):  # Start at 2, end before 11, step by 2
    print(i, end=' ')
# Output: 2 4 6 8 10

# ✅ 2) While Loop Basics
print("\n\n=== While Loop ===")
i = 0
while i <= 10:
    print(i, end=' ')
    i += 1  # Equivalent to i = i + 1
# Output: 0 1 2 3 4 5 6 7 8 9 10

# ✅ 3) Loop Control Statements
print("\n\n=== Loop Control (continue/break) ===")
for i in range(1, 20):
    if i == 3 or i == 13:
        continue  # Skip current iteration
    elif i == 19:
        break  # Exit loop completely
    print(i, end=' ')
# Output: 1 2 4 5 6 7 8 9 10 11 12 14 15 16 17 18

# ✅ 4) Nested Loops
print("\n\n=== Nested Loops ===")
for i in range(3):  # Outer loop
    for j in range(2):  # Inner loop
        print(f"({i},{j})", end=' ')
    print()  # New line after inner loop completes
# Output: (0,0) (0,1)
#         (1,0) (1,1)
#         (2,0) (2,1)

# ✅ 5) Iterating Over Collections
print("\n\n=== Iterating Over Lists ===")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit.upper(), end=' ')
# Output: APPLE BANANA CHERRY

print("\n\n=== Iterating With Index ===")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}", end=' | ')
# Output: 0: apple | 1: banana | 2: cherry |

# ✅ 6) Advanced Loop Techniques
print("\n\n=== Else Clause in Loops ===")
for i in range(5):
    print(i, end=' ')
else:
    print("\nLoop completed without break")
# Output: 0 1 2 3 4 
#         Loop completed without break

print("\n=== List Comprehensions ===")
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# ✅ 7) Common Loop Patterns
print("\n=== Accumulator Pattern ===")
total = 0
for num in [1, 2, 3, 4, 5]:
    total += num
print("Sum:", total)  # 15

print("\n=== Search Pattern ===")
found = False
for num in [3, 7, 2, 9, 5]:
    if num == 2:
        found = True
        break
print("Found 2:", found)  # True

# ✅ 8) Performance Considerations
print("\n=== Performance Tips ===")
# 1) Pre-compute values used in loop condition
# 2) Use built-in functions (sum(), max(), etc.) when possible
# 3) Avoid unnecessary computations inside loops
# 4) Consider using list comprehensions for simple transformations

# ✅ 9) Common Pitfalls
print("\n=== Common Mistakes ===")
# 1) Modifying list while iterating (create copy instead)
# 2) Infinite while loops (ensure condition will become false)
# 3) Off-by-one errors with range() bounds
# 4) Unintended variable shadowing in nested loops

# ✅ 10) Practical Examples
print("\n=== Practical Examples ===")
print("Countdown:")
for i in range(10, 0, -1):  # Countdown from 10 to 1
    print(i, end='...')
print("Liftoff!")

print("\nMultiplication Table:")
for i in range(1, 6):  # Rows
    for j in range(1, 6):  # Columns
        print(f"{i*j:2}", end=' ')  # :2 formats to 2 spaces
    print()  # New line after each row

print("\nFiltering Even Numbers:")
numbers = [12, 15, 18, 21, 24]
evens = [num for num in numbers if num % 2 == 0]
print("Even numbers:", evens)