# ⚄◉․﹒．~*~․﹒．◉⚄⚄◉․﹒．~*~․﹒．◉⚄⚄◉․﹒．~*~․﹒．◉⚄
# Tutorial 3: From Arrays to Images
# ⚄◉․﹒．~*~․﹒．◉⚄⚄◉․﹒．~*~․﹒．◉⚄⚄◉․﹒．~*~․﹒．◉⚄


# ⁌------------------------------------⁍
# What you will learn:
# ✓ visualize arrays with matplotlib
# ✓ read images with matplotlib
# ✓ manipulate images with numpy:
#   - visualize RGB channels
#   - convert to grayscale
#   - applay thresholding
#   - flip images
#   - rotate images
#   - crop images
#   - resize images
# ⁌------------------------------------⁍


import numpy as np
import matplotlib.pyplot as plt


# ~~~~~~~~~~~
# Exercise 1.1
# Use matplotlib to show the image array from Tutorial 2, Exercise 1.4.
# Hint: Use plt.imshow().
print("\n ~~~~~~~~~~~")
print("Exercise 1.1")

# ..... your code here .....

# ~~~~~~~~~~~
# Exercise 1.2
# Read the image 'data/cat.jpeg' with matplotlib.
# What is its type? What is its shape?
# Plot the image as done in Exercise 1.1.
# Hint: Use plt.imread().
print("\n ~~~~~~~~~~~")
print("Exercise 1.2")

# ..... your code here .....

# ~~~~~~~~~~~
# Exercise 1.3
# Visualize RGB channels separately.
# Hint: Use array slicing.
print("\n ~~~~~~~~~~~")
print("Exercise 1.3")

fig, ax = plt.subplots(1, 3, figsize=(15, 5))
# ..... your code here .....
ax[0].set_title('Red channel')
ax[0].axis('off')
# ..... your code here .....
ax[1].set_title('Green channel')
ax[1].axis('off')
# ..... your code here .....
ax[2].set_title('Blue channel')
ax[2].axis('off')

plt.show()  

# ~~~~~~~~~~~
# Exercise 1.4
# Convert the image from Exercise 1.2 to grayscale.
# Hint: Use the formula for grayscale: 0.2989 * R + 0.5870 * G + 0.1140 * B.
print("\n ~~~~~~~~~~~")
print("Exercise 1.4")

# ..... your code here .....

# ~~~~~~~~~~~
# Exercise 1.5
# Plot an histogram of the grayscale image from Exercise 1.4.
# Hint: Use plt.hist().
print("\n ~~~~~~~~~~~")
print("Exercise 1.5")

# ..... your code here .....

# ~~~~~~~~~~~
# Exercise 1.6
# Apply thresholding to the grayscale image from Exercise 1.4 and set all pixels below a certain threshold to 0.
# Then plot the image.
# Suggested threshold: 100.
# Hint: Use np.where().
print("\n ~~~~~~~~~~~")
print("Exercise 1.6")

# ..... your code here .....

# ~~~~~~~~~~~
# Exercise 1.7
# Flip the grayscale image from Exercise 1.4 horizontally.
# Hint: Use np.flip().
print("\n ~~~~~~~~~~~")
print("Exercise 1.7")

# ..... your code here .....

# ~~~~~~~~~~~
# Exercise 1.8
# Rotate the grayscale image from Exercise 1.4 by 45 degrees.
# Hint: Use np.rot90().
print("\n ~~~~~~~~~~~")
print("Exercise 1.8")

# ..... your code here .....

# ~~~~~~~~~~~
# Exercise 1.9
# Crop the grayscale image from Exercise 1.4 to a square of size 100x100 pixels.
# Hint: Use array slicing.
print("\n ~~~~~~~~~~~")
print("Exercise 1.9")

# ..... your code here .....

# ~~~~~~~~~~~
# Exercise 1.10
# Resize the grayscale image from Exercise 1.4 to 200x200 pixels.
# Hint: Use np.resize().
# Note: This will distort the image.
print("\n ~~~~~~~~~~~")
print("Exercise 1.10")

# ..... your code here .....



# ⚄◉․﹒．~*~․﹒．◉⚄⚄◉․﹒．~*~․﹒．◉⚄⚄◉․﹒．~*~․﹒．◉⚄
# References:
# Matplotlib documentation: https://matplotlib.org/stable/contents.html