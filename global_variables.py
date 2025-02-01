# Global Variables
# Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

# Global variables can be used by everyone, both inside of functions and outside.



x = "awesome"

def myfunc():
  x ="Ashok"#local variable
  print("Python is " + x)

myfunc()
# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

x = "global"  # this variable is global
def myfunc():
  x = "local"# this variable is local 
  print("Python is " , x)

myfunc()

print("Python is " , x)

#whenever we create the inside the global variable
# create then we write global inside the function

# example
x="AShok"
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
print("My name is:"+x)