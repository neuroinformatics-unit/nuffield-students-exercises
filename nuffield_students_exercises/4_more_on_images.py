# 🀤﹒﹒﹒✴︎﹒﹒﹒🀤﹒﹒﹒✴︎﹒﹒﹒🀤﹒﹒﹒✴︎﹒﹒﹒🀤﹒﹒﹒✴︎﹒﹒﹒🀤﹒﹒﹒✴︎﹒﹒﹒🀤﹒﹒﹒✴︎﹒﹒﹒🀤﹒﹒﹒✴︎﹒﹒﹒🀤
# Tutorial 4: more on images
# 🀤﹒﹒﹒✴︎﹒﹒﹒🀤﹒﹒﹒✴︎﹒﹒﹒🀤﹒﹒﹒✴︎﹒﹒﹒🀤﹒﹒﹒✴︎﹒﹒﹒🀤﹒﹒﹒✴︎﹒﹒﹒🀤﹒﹒﹒✴︎﹒﹒﹒🀤﹒﹒﹒✴︎﹒﹒﹒🀤

# ⁌------------------------------------⁍
# What you will learn:
# ✓ Apply thresholding to an image 2.0:
#   - Apply thresholding to different channels
#   - Apply clipping to different channels
# Stretch goals:
# ✓ Explore scikit-image library
# ⁌------------------------------------⁍


import numpy as np
import matplotlib.pyplot as plt
import skimage

# ~~~~~~~~~~~
# Exercise 1.1
# Experiment with different threshold values applied to different channels.
# Hint: Use np.where().
# The output should be a binary image (black and white).

print("\n ~~~~~~~~~~~")
print("Exercise 1.1")

threshold = 100
image = ... # load the image 'data/cat.jpeg'
channel = ... # choose a channel (0, 1, 2)
def thresholding(
        image: np.ndarray,
        threshold: int,
        RGB_channel: int
) -> np.ndarray:
    """A function that binarizes an image based on a threshold value
    for a given RGB channel.

    Parameters
    ----------
    image : np.ndarray
        The input image.
    treshold : int
        The threshold value.
    RGB_channel : int
        The channel to apply the thresholding.

    Returns
    -------
    np.ndarray
        The resulting binary image.
    """
    # ..... your code here .....
    return binary_image

binary_image = thresholding(image, threshold, channel)

fig, ax = plt.subplots(1, 3, figsize=(10, 5))
ax[0].imshow(image)
ax[0].set_title('Original image')
ax[0].axis('off')
ax[1].imshow(binary_image, cmap='gray')
ax[1].set_title(f'Binary image, threshold = {threshold}, channel = {channel}')
ax[1].axis('off')
ax[2].hist(image[:,:,channel].ravel(), bins=256, color='k')
ax[2].axvline(threshold, color='r')
ax[2].set_title(f'Histogram of channel {channel}')

plt.show()

# ~~~~~~~~~~~
# Exercise 1.2
# Set a lower and upper threshold value.
# Hint: Use np.logical_and().
# The output should be a binary image (black and white).
print("\n ~~~~~~~~~~~")
print("Exercise 1.2")

lower_treshold = ... # set a lower threshold value
upper_treshold = ... # set an upper threshold value
def clipping_on_RGB_channel(
        image: np.ndarray,
        lower_treshold: int,
        upper_treshold: int,
        RGB_channel: int
) -> np.ndarray:
    """Apply clipping to an image based on a lower and upper threshold value
    for a given RGB channel.
    Clipping is a process of limiting the values of an image to a certain range.
    It is useful for removing noise from the image.

    Parameters
    ----------
    image : np.ndarray
        The input image.
    lower_treshold : int
        The lower threshold value.
    upper_treshold : int
        The upper threshold value.

    RGB_channel : int
        The channel to apply the thresholding.
    
    Returns
    -------
    np.ndarray
        The resulting binary image.
    """
    # ..... your code here .....
    return binary_image

binary_image = clipping_on_RGB_channel(image, lower_treshold, upper_treshold, channel)

fig, ax = plt.subplots(1, 3, figsize=(10, 5))
ax[0].imshow(image)
ax[0].set_title('Original image')
ax[0].axis('off')
ax[1].imshow(binary_image, cmap='gray')
ax[1].set_title(f'Binary image, lower threshold = {lower_treshold}, upper threshold = {upper_treshold}, channel = {channel}')
ax[1].axis('off')
ax[2].hist(image[:,:,channel].ravel(), bins=256, color='k') 
ax[2].axvline(lower_treshold, color='r')
ax[2].axvline(upper_treshold, color='r')
ax[2].set_title(f'Histogram of channel {channel}')

plt.show()


# 🀤﹒﹒﹒✴︎﹒﹒﹒🀤﹒﹒﹒✴︎﹒﹒﹒🀤﹒﹒﹒✴︎﹒﹒﹒🀤﹒﹒﹒✴︎﹒﹒﹒🀤﹒﹒﹒✴︎﹒﹒﹒🀤﹒﹒﹒✴︎﹒﹒﹒🀤﹒﹒﹒✴︎﹒﹒﹒🀤
# Stretch goals
# 🀤﹒﹒﹒✴︎﹒﹒﹒🀤﹒﹒﹒✴︎﹒﹒﹒🀤﹒﹒﹒✴︎﹒﹒﹒🀤﹒﹒﹒✴︎﹒﹒﹒🀤﹒﹒﹒✴︎﹒﹒﹒🀤﹒﹒﹒✴︎﹒﹒﹒🀤﹒﹒﹒✴︎﹒﹒﹒🀤

# In the scikit-image library, there are many functions for image processing.
# There is a list of examples of what you can do with scikit-image: 
# https://scikit-image.org/docs/stable/auto_examples/index.html
# Chose one example on the following cathegories and try to implement it on the 'data/neurons.npy' image:
# - Manipulating exposure and color channels
# - Edges and lines
# - Detection of features and objects
# Hint: first load the image with np.load().

