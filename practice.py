# ---------------------escape sequence--------------------
print("hello \
world")
print("hello \\")
print("hello \"")
print("hello \'")
print("hello \"prity\" girl")
print("hello \nworld")
print("hello world\b")
print("hello world\rrevathi")
print("hello\tworld")
print("hello \a")
print("hello \fworld")
print("hello \fworld \fworld")
print("hello \104")
print("hello \x41")
print("\N{BLACK HEART SUIT}")
print("\U0001F600") #32 bits
print("\u03A9") #16 bits

#----------------concatenation-----------
print("hello " 'world')
print("""
i am revathi
employee in google
""")
a = "hello "
b = "world"
print(a + b)
words = ["i ", "am ", "revathi "]
j = "".join(words)
print(j)

#--------------------fstring-------------
print(f"name= {"i am revathi", "employee in google"}")
print(f"name= {"i am revathi"}")
name = "python"
print(f"my name is {name !r}")
print(f"my name is {repr(name)}")
line = "i am 'revathi'"
print(f"{line = !r:20}")
print(f"{line = }")
line = "The mill's closed"
print(f"{line = }")
a = dict(x=2)
print(f"abc {a["x"]} def")

a = ['1', '2', '3', '4']
print(f"list of numbers :\n {"\n ".join(a)}")

#-----------operators----------------
if (n := 10) > 3:
    print(n)

print(5 & 3)     # &  → AND → 1   (0101 & 0011 = 0001)
print(5 | 3)     # |  → OR → 7    (0101 | 0011 = 0111)
print(5 ^ 3)     # ^  → XOR → 6   (0101 ^ 0011 = 0110)
print(~5)        # ~  → bitwise NOT → -6
print(5 << 1)    # << → shift left  → 10   (0101 << 1 = 1010)
print(5 >> 1)

import numpy as np

A = np.array([[1, 2],
              [3, 4]])
B = np.array([[2, 2],
              [1, 2]])

print(A @ B)

a = 5; b= 5 ; print(a+b)

import gc

gc.enable(count0, count1, count2)