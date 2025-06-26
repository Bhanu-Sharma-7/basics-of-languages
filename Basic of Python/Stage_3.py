# 1) Arithmetic Operators
print("Arithmetic Operators:")
# Basic math operations
print(1 + 2)    # Addition: 3
print(1 - 2)    # Subtraction: -1
print(1 * 2)    # Multiplication: 2
print(1 / 2)    # Division: 0.5 (float result)
print(1 // 2)   # Floor Division: 0 (integer part only)
print(1 ** 2)   # Exponentiation: 1^2 = 1
print(1 % 2)    # Modulus: remainder = 1

# 2) Assignment Operators
print("\nAssignment Operators:")
a = 1
print(a)        # a = 1
a += 1
print(a)        # a = 2
a -= 1
print(a)        # a = 1
a *= 1
print(a)        # a = 1
a /= 1
print(a)        # a = 1.0
a //= 1
print(a)        # a = 1.0 (still float after floor division)
a %= 1
print(a)        # a = 0.0 (1 % 1 = 0)
a **= 1
print(a)        # a = 0.0 ** 1 = 0.0

# 3) Comparison Operators
print("\nComparison Operators")
print(3 == 3)   # Equal to → True
print(3 != 3)   # Not equal to → False
print(3 <= 3)   # Less than or equal to → True
print(3 >= 3)   # Greater than or equal to → True
print(3 < 3)    # Less than → False
print(3 > 3)    # Greater than → False

# 4) Logical Operators
print("\nLogical Operators:")
print(3 == 3 and 3 == 3)  # True and True → True
print(3 == 3 and 3 != 3)  # True and False → False
print(3 == 3 or 3 != 3)   # True or False → True
print(3 != 3 or 3 != 3)   # False or False → False
