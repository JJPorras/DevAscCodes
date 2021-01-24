# Fill in this file with the code from the introduction to Python
import math
import random
# TRYIT: Write a print statement that displays both the type and value of Pi
pi = math.pi
print("pi is a {} with a value of {}".format(type(pi), pi))
# TRYIT: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
if i > 50:
      print("Greater than 50")
elif i < 50:
      print("Less that 50")
else:
      print("Equal to 50")
# TRYIT: Write a conditional that prints the color of the picked fruit
fruit = random.choice(['Naranja', 'Banana', 'Apple'])
print(fruit)
# TRYIT: Write a function that multiplies two numbers and returns the result
def multiplies(num1, num2):
      return num1*num2
# TRYIT: Write a function that multiplies two numbers and returns the result
def add(num1, num2):
      return num1+num2
# TRYIT: Now call the function a few times to calculate the following answers
print(multiplies(5, 50))
print(add(50, 5))  
