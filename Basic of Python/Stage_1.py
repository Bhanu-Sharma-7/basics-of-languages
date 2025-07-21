Python print() Function – Complete & Easy Guide

1) Simple Text Print Karna

print("Hello, My name is Bhanu Sharma")

Output:

Hello, My name is Bhanu Sharma

Explanation: Double quotes ke andar jo likha, woh print ho gaya.


---

2) Variable Print Karna

name = "Bhanu"
print(name)

Output:

Bhanu

Explanation: name ek variable hai jisme "Bhanu" store hai, print(name) se woh value print hoti hai.


---

3) Text + Variable Saath Me Print Karna

name = "Bhanu"
print("Hello, my name is", name, "Sharma")

Output:

Hello, my name is Bhanu Sharma

Explanation: Comma (,) ka use kiya multiple cheezen print karne ke liye.


---

4) Escape Characters ka Use

print("Hello\nWorld")

Output:

Hello
World

Explanation: \n ka matlab hai new line (nayi line me likhna).


---

5) Empty Line Print Karna

print()

Output: (blank line)

Explanation: Jab kuch bhi nahi hota print() ke andar, ek khali line print hoti hai.


---

6) sep (Separator) aur end ka Use

print("Python", "Java", "C++", sep=" | ")

Output:

Python | Java | C++

Explanation: sep se hum decide karte hain ki beech me kya aaye.

print("Going to", end=" --> ")
print("Goa")

Output:

Going to --> Goa

Explanation: Normally, print ke baad new line hoti hai, lekin end=" --> " diya to wahi likha aayega instead of \n.


---

7) f-Strings – Best Way to Mix Variables

name = "Bhanu"
age = 20
print(f"My name is {name}, and I am {age} years old.")

Output:

My name is Bhanu, and I am 20 years old.

Explanation: f-string me {} ke andar variable rakhte hain, aur string automatic form hoti hai.


---

(Bonus) Printing with + Operator (Concatenation)

name = "Bhanu"
print("Hello, my name is " + name)

Output:

Hello, my name is Bhanu

Explanation: + tab kaam karega jab sab cheezein string ho.


---

Final Tips:

, (comma) auto space deta hai between items.

+ direct join karta hai but sabko string hona chahiye.

f-string is clean, modern and recommended way.



---

Next Step: Practice using these concepts with your own variables and messages. Agar PDF ya practice exercise chahiye ho to bolo! 🚀

