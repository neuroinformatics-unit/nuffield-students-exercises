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

array1_1 = np.arange(1, 101)
print(array1_1)

# ~~~~~~~~~~~
# Exercise 1.2
# Make a 2D numpy array of shape (10, 10) with all elements set to 0.
# Hint: Use np.zeros().
print("\n ~~~~~~~~~~~")
print("Exercise 1.2")

b = np.zeros((10, 10))
print(b)

# ~~~~~~~~~~~
# Exercise 1.3
# Change the element in the 5th row and 5th column of the array from Exercise 1.2 to 1.
# Hint: Use array indexing.
print("\n ~~~~~~~~~~~")
print("Exercise 1.3")

b[4][4] = 1
print(b)

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

# Using np.ones()
array1_4 = np.ones((10, 10))
array1_4[1:9, 1:9] = 0
print(f"Solution 1: \n{array1_4}")

# Using np.zeros()
c = np.zeros((10, 10))
c[0:1] = 1
c[9:10] = 1
c[:, 0] = 1
c[:, 9] = 1

print(f"Solution 2: \n{c}")

# ~~~~~~~~~~~
# Exercise 1.5
# Add the two arrays from Exercise 1.3 and Exercise 1.4.
# Hint: Use the + operator.
print("\n ~~~~~~~~~~~")
print("Exercise 1.5")

array1_5 = b + c

print(array1_5)

# ~~~~~~~~~~~
# Exercise 1.6
# Multiply the array from Exercise 1.5 by 2.
# Hint: Use the * operator.
print("\n ~~~~~~~~~~~")
print("Exercise 1.6")

array1_6 = array1_5 * 2
print(array1_6)

# ~~~~~~~~~~~
# Exercise 1.7
# Calculate the mean, median, and standard deviation of the array from Exercise 1.6.
# Hint: Use np.mean(), np.median(), and np.std().
print("\n ~~~~~~~~~~~")
print("Exercise 1.7")

print(f"The mean of the matrix is: {np.mean(array1_6)}")
print(f"The median of the matrix is: {np.median(array1_6)}")
print(f"The standard deviation of the matrix is: {np.std(array1_6):.2f}")

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

print(a.shape)
print(b.shape)
print(a[:, np.newaxis].shape)
print(result.shape)

# ☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎☐◼︎
# References:
# Numpy quickstart tutorial: https://numpy.org/doc/stable/user/quickstart.html
# Numpy broadcasting: https://numpy.org/doc/stable/user/basics.broadcasting.html
