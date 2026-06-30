# Operators

# Arithmetic Operators
a = 11
b = 2
c = 5
d = 76

# +  Addition
print(a+b)

# -  Subtraction
print(c-b)

# *  Multiplication
print(c*d)

# / Division
print(d/c)

# //  Floor Division
print(d//c)

# %  Modulus
print(d%c)

# **  Exponent
print(c**b)


# Comparison Operators (Return True or False)

print(a == 11)
print(a != 11)
print(a > 5)
print(a < 11)
print(a <= 11)
print(a >= 11)

# Logical Operators
age =  14
# and Both conditions must be true
print("and", age >= 18 and age <= 25)

# or At least one condition is true
print("or", age>18 or age==18)

# not Reverse the Boolean value
print("not", not(age >= 18))

# Bitwise Operators (Operate on the binary representation of integers)
a = 5      # 0101
b = 3      # 0011

print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 1)
print(a >> 1)

# Identity Operators (is, is not)
m = [1, 2]
n = m
f = [1, 2]

print(m is n)
print(m == f)
print(m is f)
print(m is not n)

# Membership Operators (in, not in)
fruits = ["apple", "banana"]
print("apple is in fruits array :", "apple" in fruits)
print("banana is in fruits array :", "banana" not in fruits)