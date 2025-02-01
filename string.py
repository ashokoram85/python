# Strings in python are surrounded by either single quotation marks, or double quotation marks.

# 'hello' is the same as "hello".

# You can display a string literal with the print() function:

print("hye my name is ashok")


# multiline strings
a = """ hye my name is ashok and i have completed my b.tech degree,
 2027 and corrently i got a part time job and my salary 60k per month,
 then i would like to say something.."""

print(a)

# strings are arrays
a = "Hello,ashok"
print(a[1:]) # word written


# looping through a string

for x in "Ashok":
  print(x) #loop through Ashok

# string length
a ="ashok fuck u"
print(len(a))  

#check string
name = "Hello Ashok"
print("u" in a) #having the string which is print

name ="My name is Ashok"
if "name" in name:
  print("yes,my 'name' is Ashok.")

# check if not
name ="My name is ashok"
print("fuck" not in name)