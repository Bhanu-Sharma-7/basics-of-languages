# ✅ 1) List ka use:
# Ek hi variable ke andar multiple data store karne ke liye use hoti hai list
names = ["Bhanu", "Sandeep", "Abhay", "Devansh"]
print("Names List:", names)

# ✅ 2) Indexing in List:
# Indexing 0 se start hoti hai
print("Index 0:", names[0])
print("Index 1:", names[1])

# ✅ 3) Negative Indexing:
# -1 means last item, -2 means second last, and so on
print("Last item (negative indexing):", names[-1])

# ✅ 4) Creating List of Numbers:
numbers = [1, 2, 3, 4, 5, 6, 7]

# ✅ 5) Slicing:
# Syntax: list[start_index : end_index] (end index excluded)
print("Index 1 to 3:", numbers[1:4])  # Output: [2, 3, 4]
print("First 3 items:", numbers[:3])  # Output: [1, 2, 3]
print("From index 3 to end:", numbers[3:])  # Output: [4, 5, 6, 7]

# ✅ 6) Common List Functions:
my_list = [1, 2, 3, 5, 6, 3, 2, 1, 4, 2, 5, 2, 4, 2, 1]

# 👉 append(): last me item add karta hai
my_list.append(12)
print("After append(12):", my_list)

# 👉 pop(): last item remove karta hai
my_list.pop()
print("After pop():", my_list)

# 👉 insert(index, value): specific index par value insert karta hai
my_list.insert(1, 15)
print("After insert(1, 15):", my_list)

# 👉 reverse(): list ko ulta kar deta hai
my_list.reverse()
print("After reverse():", my_list)

# 👉 sort(): list ko ascending order me sort karta hai
my_list.sort()
print("After sort():", my_list)

# ✅ 7) Mixed Data Type List:
# List me alag-alag data types ka collection possible hai
multi_list = [1, "Bhanu", True, None]
print("Mixed Type List:", multi_list)
