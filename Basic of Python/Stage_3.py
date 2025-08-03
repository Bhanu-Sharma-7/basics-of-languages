# ============== PYTHON OPERATORS COMPREHENSIVE GUIDE ==============

# ✅ 1) Arithmetic Operators
print("\n=== ARITHMETIC OPERATORS ===")
print("Basic math operations:")
print("Addition (5 + 3):", 5 + 3)        # 8
print("Subtraction (5 - 3):", 5 - 3)     # 2
print("Multiplication (5 * 3):", 5 * 3)  # 15
print("Division (5 / 3):", 5 / 3)        # 1.666... (always returns float)
print("Floor Division (5 // 3):", 5 // 3) # 1 (rounds down to nearest integer)
print("Exponentiation (5 ** 3):", 5 ** 3) # 125 (5 to the power of 3)
print("Modulus (5 % 3):", 5 % 3)         # 2 (remainder after division)

# Special cases
print("\nSpecial cases:")
print("Division by zero (5 / 0):", "ZeroDivisionError") # Raises error
print("Negative exponent (4 ** -2):", 4 ** -2) # 0.0625 (1/(4^2))
print("Modulus with negative (5 % -3):", 5 % -3) # -1 (follows sign of divisor)

# ✅ 2) Assignment Operators
print("\n=== ASSIGNMENT OPERATORS ===")
x = 10
print("Initial x =", x)

x += 5  # Equivalent to x = x + 5
print("After x += 5:", x)  # 15

x -= 3  # x = x - 3
print("After x -= 3:", x)  # 12

x *= 2  # x = x * 2
print("After x *= 2:", x)  # 24

x /= 4  # x = x / 4 (converts to float)
print("After x /= 4:", x)  # 6.0

x //= 2 # x = x // 2
print("After x //= 2:", x) # 3.0

x **= 3 # x = x ** 3
print("After x **= 3:", x) # 27.0

x %= 5  # x = x % 5
print("After x %= 5:", x)  # 2.0

# Multiple assignment
a, b, c = 1, 2, 3
print("\nMultiple assignment:")
print(f"a={a}, b={b}, c={c}")

# Swapping values
a, b = b, a
print("After swap: a={}, b={}".format(a, b))

# ✅ 3) Comparison Operators
print("\n=== COMPARISON OPERATORS ===")
print("Equal (5 == 5):", 5 == 5)       # True
print("Not equal (5 != 5):", 5 != 5)   # False
print("Less than (5 < 5):", 5 < 5)     # False
print("Greater than (5 > 5):", 5 > 5)  # False
print("Less than or equal (5 <= 5):", 5 <= 5) # True
print("Greater than or equal (5 >= 5):", 5 >= 5) # True

# Chained comparisons
print("\nChained comparisons (5 < 10 <= 15):", 5 < 10 <= 15) # True
print("Chained comparisons (5 < 10 > 8):", 5 < 10 > 8) # True

# Comparing different types
print("\nType comparison (5 == 5.0):", 5 == 5.0) # True (value equality)
print("Identity comparison (5 is 5.0):", 5 is 5.0) # False (different objects)

# ✅ 4) Logical Operators
print("\n=== LOGICAL OPERATORS ===")
print("AND (True and False):", True and False)  # False
print("OR (True or False):", True or False)    # True
print("NOT (not True):", not True)             # False

# Short-circuit evaluation
print("\nShort-circuit behavior:")
def return_false():
    print("return_false called")
    return False

def return_true():
    print("return_true called")
    return True

print("False and ...:", False and return_false())  # Doesn't call function
print("True or ...:", True or return_true())      # Doesn't call function

# Practical examples
age = 25
has_license = True
print("\nPractical example (age >= 18 and has_license):", 
      age >= 18 and has_license)  # True

# ✅ 5) Bitwise Operators
print("\n=== BITWISE OPERATORS ===")
a = 0b1010  # 10 in binary
b = 0b1100  # 12 in binary

print("AND (a & b):", bin(a & b))    # 0b1000 (8)
print("OR (a | b):", bin(a | b))     # 0b1110 (14)
print("XOR (a ^ b):", bin(a ^ b))    # 0b0110 (6)
print("NOT (~a):", ~a)               # -11 (two's complement)
print("Left shift (a << 2):", bin(a << 2)) # 0b101000 (40)
print("Right shift (a >> 1):", bin(a >> 1)) # 0b0101 (5)

# ✅ 6) Membership Operators
print("\n=== MEMBERSHIP OPERATORS ===")
fruits = ['apple', 'banana', 'cherry']
print("'banana' in fruits:", 'banana' in fruits)       # True
print("'orange' not in fruits:", 'orange' not in fruits) # True

# Works with strings
print("'pp' in 'apple':", 'pp' in 'apple')  # True

# ✅ 7) Identity Operators
print("\n=== IDENTITY OPERATORS ===")
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print("x is z:", x is z)       # True (same object)
print("x is y:", x is y)       # False (different objects)
print("x == y:", x == y)       # True (equivalent values)

# None comparison
var = None
print("var is None:", var is None)  # True (preferred way to check for None)

# ✅ 8) Operator Precedence
print("\n=== OPERATOR PRECEDENCE ===")
result = 5 + 3 * 2 ** 2 / 4 - 1
print("5 + 3 * 2 ** 2 / 4 - 1 =", result)  # 7.0
# Order: ** → * / // % → + -

# Use parentheses to override
print("(5 + 3) * 2 =", (5 + 3) * 2)  # 16

# ✅ 9) Walrus Operator (Python 3.8+)
print("\n=== WALRUS OPERATOR (:=) ===")
if (n := len(fruits)) > 2:
    print(f"There are {n} fruits in the list")  # Prints the message

# Useful in while loops
while (input_val := input("Enter 'quit' to exit: ")) != 'quit':
    print("You entered:", input_val)

# ✅ 10) Practical Applications
print("\n=== PRACTICAL APPLICATIONS ===")
# Calculate area of circle
radius = 5
area = 3.14159 * radius ** 2
print(f"Area of circle with radius {radius}: {area:.2f}")

# Check if number is even
num = 10
print(f"{num} is even:", num % 2 == 0)

# Convert Fahrenheit to Celsius
fahrenheit = 77
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit}°F = {celsius:.1f}°C")

# Ternary operator
age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Age {age} status: {status}")