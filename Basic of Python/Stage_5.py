# 1) if and else
age = 18

if age >= 18:
    print("You can drive")
else:
    print("You cannot drive")

# 2) elif (else if)
if age < 0:
    print("Given age is incorrect, please enter a valid age")
elif age >= 18:
    print("You can drive")
else:
    print("You cannot drive")

# 3) Nested if else
age = 18

if age <= 0:
    print("Please enter a valid age")
elif age >= 18:
    print("You can drive")
    if age >= 20:
        print("You can do a job")
    else:
        print("You cannot do a job")
else:
    print("You cannot drive")
