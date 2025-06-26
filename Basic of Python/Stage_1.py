# 1) Basic print() Syntax
# Ek simple text ko print karna
print("Hello, My name is Bhanu Sharma")

# 2) Printing a Variable
# Pehle variable banaya, fir usse print kiya
name = "Bhanu"
print(name)

# 3) Printing Text + Variable Together
# Text aur variable ko ek sath print karne ke liye , (comma) ka use kiya
name = "Bhanu"
print("Hello, My name is", name, "Sharma")

# 4) Using Escape Characters
# \n ka matlab hota hai new line, yani next line me likhna start karega
print("Hello\nworld")

# 5) Using print() without Anything
# Agar print() ke andar kuch nahi likha to woh sirf ek khali line print karega
print()

# 6) Customizing Separator (sep) and Ending (end)
# sep ka use hota hai alag-alag values ke beech me separator lagane ke liye
print("Python", "Java", "C++", sep=" | ")  # output: Python | Java | C++

# end ka use hota hai ki print ke baad kya aana chahiye (default "\n" hota hai)
print("Going to", end=" --> ")
print("Goa")  # output: Going to --> Goa

# 7) Using print() with f-strings (Formatted Strings)
# f-string se hum variables ko directly {} ke andar use kar sakte hain
name = "Bhanu"
age = 20
print(f"My name is {name}, and I am {age} years old.")
