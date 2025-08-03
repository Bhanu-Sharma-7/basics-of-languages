# ============== PYTHON CONDITIONAL STATEMENTS GUIDE ==============

# ✅ 1) Basic if-else Statement
print("\n=== BASIC IF-ELSE ===")
age = 18

# Simple age check
if age >= 18:
    print("You can drive")      # This will execute
else:
    print("You cannot drive")

# Truthy/Falsy evaluation
print("\nTruthy/Falsy evaluation:")
name = "Bhanu"
if name:  # Equivalent to if bool(name) == True
    print(f"Hello, {name}")    # Will execute for non-empty strings
else:
    print("No name provided")

# ✅ 2) elif (else if) Statement
print("\n=== ELIF STATEMENT ===")
score = 85

# Grade classification
if score >= 90:
    print("Grade: A")
elif score >= 80:  # Only checked if first condition is False
    print("Grade: B")  # This will execute
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: D or F")

# Multiple conditions
temperature = 22
humidity = 65

if temperature > 30 and humidity > 70:
    print("Hot and humid day")
elif temperature > 25 or humidity > 60:
    print("Warm or somewhat humid")  # This will execute
else:
    print("Pleasant weather")

# ✅ 3) Nested Conditionals
print("\n=== NESTED CONDITIONALS ===")
age = 20
has_license = True

if age >= 18:
    print("You meet the age requirement")
    if has_license:
        print("You can drive legally")  # This will execute
    else:
        print("You need to get a license first")
else:
    print("You're too young to drive")

# Complex nested example
balance = 1500
is_premium = True
withdrawal = 1200

if balance >= withdrawal:
    print("Withdrawal possible")
    if is_premium:
        print("No fees charged")  # This will execute
    else:
        if withdrawal > 1000:
            print("$5 fee applied")
        else:
            print("No fees for small withdrawals")
else:
    print("Insufficient funds")

# ✅ 4) Ternary Operator
print("\n=== TERNARY OPERATOR ===")
# Traditional if-else
if age >= 18:
    status = "Adult"
else:
    status = "Minor"

# Ternary equivalent
status = "Adult" if age >= 18 else "Minor"
print(f"Status: {status}")  # Adult

# Nested ternary (use sparingly)
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D or F"
print(f"Your grade is: {grade}")

# ✅ 5) Match-Case (Python 3.10+)
print("\n=== MATCH-CASE ===")
# Alternative to complex if-elif chains
http_status = 404

match http_status:
    case 200:
        print("Success")
    case 400:
        print("Bad request")
    case 404:
        print("Not found")  # This will execute
    case 500:
        print("Server error")
    case _:  # Default case
        print("Unknown status code")

# ✅ 6) Boolean Expressions
print("\n=== BOOLEAN EXPRESSIONS ===")
# Combining conditions
is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("No work today!")  # This will execute

# De Morgan's Laws
has_permission = False
is_admin = True

if not (has_permission and is_admin):
    print("Access denied")  # Equivalent to (not has_permission) or (not is_admin)

# ✅ 7) Common Pitfalls
print("\n=== COMMON PITFALLS ===")
# 1. Using assignment (=) instead of equality (==)
x = 5
if x == 5:  # Correct
    print("x is 5")

# 2. Chained comparisons
if 18 <= age < 65:  # Correct way
    print("Working age")

# 3. Truthy checks
empty_list = []
if not empty_list:  # Preferred over len(empty_list) == 0
    print("List is empty")

# ✅ 8) Practical Applications
print("\n=== PRACTICAL APPLICATIONS ===")
# Password strength checker
password = "SecureP@ss123"
if len(password) >= 8 and any(c.isupper() for c in password) \
   and any(c.isdigit() for c in password) and not password.isalnum():
    print("Strong password")
else:
    print("Weak password")

# Temperature alert system
temp = -5
if temp > 30:
    print("Heat warning!")
elif temp < 0:
    print("Freezing warning!")  # This will execute
elif temp > 25:
    print("Warm day ahead")
else:
    print("Normal temperatures")

# ✅ 9) Best Practices
"""
1. Keep conditions simple and readable
2. Avoid deeply nested conditionals (consider functions)
3. Use parentheses for complex expressions
4. Put most likely conditions first in if-elif chains
5. Use match-case for multiple exact value comparisons (Python 3.10+)
6. Avoid negative conditions when possible (if not invalid vs if valid)
7. Use early returns to reduce nesting
"""

# Early return example (in function context)
def process_data(data):
    if not data:  # Guard clause
        return "No data provided"
    
    # Main processing here
    return "Data processed successfully"

# ✅ 10) Real-world Example: User Access Control
print("\n=== USER ACCESS CONTROL EXAMPLE ===")
user_role = "editor"
is_authenticated = True
article_owner = "bhanu"
current_user = "bhanu"

if is_authenticated:
    if user_role == "admin":
        print("Full access granted")
    elif user_role == "editor":
        if article_owner == current_user:
            print("Edit access to your own articles")  # This will execute
        else:
            print("Read-only access to others' articles")
    else:
        print("Basic read access")
else:
    print("Please log in first")