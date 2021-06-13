x = "Hello"
y = "World"

# concatenation
z = x + " " + y

print(z)

# string + int
a = "yushan"
b = 5

# print(a + b) [Error - can only concatenate str (not "int") to str]

# string * int
a = "yushan"
b = 2

print(a * b)

# converted to integer type
a = int("10")
b = 2

print(a + b)

# converted to float type
a = float("7.1")
b = 3

print(a + b)

# converted to bool type
a = "False"
b = 10

a = bool(a)
print(a)

c = a + b

print(c)