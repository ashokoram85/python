# there are numberic type in python
x= 9
y=3.4
z= 1j
print(type(x)) #int
print(type(y)) #float
print(type(z)) #complex

# Float can also be scientific numbers with an "e" to indicate the power of 10.


num =float(x)
num1 =int (y)
# num2 =int (z)
print(type(num))
print(type(num1))
# print(type(num2))
# You cannot convert complex numbers into another number type.
# python does not have a random() function to make a random number
# but python has a built-in module called random that can be used to make
# random numbers:

import random
print(random.randrange(1, 10)) # this will give the answer is random value

