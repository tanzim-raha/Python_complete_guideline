#Python Operators

""" Arithmetic operators // +,-
Assignment operators, =
Comparison operators
Logical operators
Membership operators
Bitwise operators"""
#Arithmetic
a=10
b=3
print(a + b)   # 13  (Addition)
print(a - b)   # 7   (Subtraction)
print(a * b)   # 30  (Multiplication)
print(a / b)   # 3.33 (Division)
print(a % b)   # 1   (Modulus)
print(a ** b)  # 1000 (Power)
print(a // b)  # 3   (Floor Division) point ar agar man bose
#assignment
x = 5
x += 3   # x = x + 3 → 8
print(x)
x -= 2  # 6
print(x)
x *= 2   # 12
print(x)
x /= 3   # 4.0
print(x)

#comparison 

print(a == b)  # False
print(a != b)  # True
print(a > b)   # False
print(a < b)   # True
print(a >= 5)  # True
print(a <= 3)  # False

#logical
p = True
q = False

print(p and q)  # False
print(p or q)   # True
print(not p)    # False

#bitwise
c = 5   # 0101
d = 3   # 0011

print(c & d)  # 1  (AND)
print(c | d)  # 7  (OR)
print(c ^ d)  # 6  (XOR)
print(~c)     # -6 (NOT)
print(c << 1) # 10 (Left shift)
print(c >> 1) # 2  (Right shift)

