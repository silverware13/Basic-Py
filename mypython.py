# By Zachary Thomas
# Python Exploration
# 1/22/2018

# Import modules.
from __future__ import print_function
import random
import string

# Set our string to all lowercase letters.
string.ascii_letters
'abcdefghijklmnopqrstuvwxyz'

# Generate three strings with ten random letters.
s1=""
s2=""
s3=""
for x in range(0,10):
	s1+= random.choice(string.ascii_lowercase)
for x in range(0,10):
	s2+= random.choice(string.ascii_lowercase)
for x in range(0,10):
	s3+= random.choice(string.ascii_lowercase)

# Create three text files.
t1= open("textOne.txt","w+")
t2= open("textTwo.txt","w+")
t3= open("textThree.txt","w+")

# Write random letters to our text files.
t1.write(s1 + "\n")
t2.write(s2 + "\n")
t3.write(s3 + "\n")

# Display our random letters.
print (s1)
print (s2)
print (s3)

# Close our text files.
t1.close()
t2.close()
t3.close()

# Get two random ints whose range is from 1 to 42 and display them.
i1= random.randint(1,42)
i2= random.randint(1,42)
print(i1)
print(i2)

# Find the product of our two numbers and display it.
i3= i1 * i2
print(i3)
