# ☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎
# Tutorial 2: Introduction to Numpy
# ☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎


# ⁌------------------------------------⁍
# What you will learn:
# ✓ create numpy arrays
# ✓ manipulate numpy arrays (indexing, slicing)
# ✓ change elements in numpy arrays
# ✓ operations on numpy arrays
# ✓ mean, median, and standard deviation
# ✓ intro to broadcasting
# ⁌------------------------------------⁍



import numpy as np


# ~~~~~~~~~~~
# Exercise 1.1
# Create a numpy array of the numbers from 1 to 100.
# Hint: Use np.arange().
print("\n ~~~~~~~~~~~")
print("Exercise 1.1")

# ..... your code here .....

# ~~~~~~~~~~~
# Exercise 1.2
# Make a 2D numpy array of shape (10, 10) with all elements set to 0.
# Hint: Use np.zeros().
print("\n ~~~~~~~~~~~")
print("Exercise 1.2")

# ..... your code here .....

# ~~~~~~~~~~~
# Exercise 1.3
# Change the element in the 5th row and 5th column of the array from Exercise 1.2 to 1.
# Hint: Use array indexing.
print("\n ~~~~~~~~~~~")
print("Exercise 1.3")

# ..... your code here .....

# ~~~~~~~~~~~
# Exercise 1.4
# Create an array which borders are set to 1 and the inside is set to 0.
# The array should have shape (10, 10).
# Hint: Use array slicing.
# Visual representation:
# 1 1 1 1 1 1 1 1 1 1 
# 1 0 0 0 0 0 0 0 0 1
# 1 0 0 0 0 0 0 0 0 1
# 1 0 0 0 0 0 0 0 0 1
# 1 0 0 0 0 0 0 0 0 1
# 1 0 0 0 0 0 0 0 0 1
# 1 0 0 0 0 0 0 0 0 1
# 1 0 0 0 0 0 0 0 0 1
# 1 0 0 0 0 0 0 0 0 1
# 1 1 1 1 1 1 1 1 1 1 
print("\n ~~~~~~~~~~~")
print("Exercise 1.4")

# ..... your code here .....

# ~~~~~~~~~~~
# Exercise 1.5
# Add the two arrays from Exercise 1.3 and Exercise 1.4.
# Hint: Use the + operator.
print("\n ~~~~~~~~~~~")
print("Exercise 1.5")

# ..... your code here .....

# ~~~~~~~~~~~
# Exercise 1.6
# Multiply the array from Exercise 1.5 by 2.
# Hint: Use the * operator.
print("\n ~~~~~~~~~~~")
print("Exercise 1.6")

# ..... your code here .....

# ~~~~~~~~~~~
# Exercise 1.7
# Calculate the mean, median, and standard deviation of the array from Exercise 1.6.
# Hint: Use np.mean(), np.median(), and np.std().
print("\n ~~~~~~~~~~~")
print("Exercise 1.7")

# ..... your code here .....

# ~~~~~~~~~~~
# Exercise 1.8
# Here we sum two arrays of different shapes.
# What was the shape of the original arrays?
# What is the shape of the resulting array? 
# See array broadcasting for more information.
print("\n ~~~~~~~~~~~")
print("Exercise 1.8")

a = np.array([0.0, 10.0, 20.0, 30.0])
b = np.array([1.0, 2.0, 3.0])
result =  a[:, np.newaxis] + b

# ..... your code here .....

# ☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎
# References:
# Numpy quickstart tutorial: https://numpy.org/doc/stable/user/quickstart.html
# Numpy broadcasting: https://numpy.org/doc/stable/user/basics.broadcasting.html
