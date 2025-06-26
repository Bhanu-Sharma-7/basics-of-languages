# 1) For Loop: 0 se 9 tak numbers print karega
for i in range(10):
    print(i)

print()  # Line break

# 2) While Loop: 0 se 10 tak numbers print karega
i = 0
while i <= 10:
    print(i)
    i += 1

print()  # Line break

# 3) For Loop with Condition: 1 se 19 tak print karega lekin 3 aur 13 skip karega
for i in range(1, 20):
    if i == 3 or i == 13:
        continue
    elif i == 19:
        break
    print(i)

print()  # Line break
