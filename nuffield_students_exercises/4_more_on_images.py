# 🀤﹒﹒﹒✴︎﹒﹒﹒🀤﹒﹒﹒✴︎﹒﹒﹒🀤﹒﹒﹒✴︎﹒﹒﹒🀤﹒﹒﹒✴︎﹒﹒﹒🀤﹒﹒﹒✴︎﹒﹒﹒🀤﹒﹒﹒✴︎﹒﹒﹒🀤﹒﹒﹒✴︎﹒﹒﹒🀤
# Tutorial 4: more on images
# 🀤﹒﹒﹒✴︎﹒﹒﹒🀤﹒﹒﹒✴︎﹒﹒﹒🀤﹒﹒﹒✴︎﹒﹒﹒🀤﹒﹒﹒✴︎﹒﹒﹒🀤﹒﹒﹒✴︎﹒﹒﹒🀤﹒﹒﹒✴︎﹒﹒﹒🀤﹒﹒﹒✴︎﹒﹒﹒🀤

# ⁌------------------------------------⁍
# What you will learn:
# ✓ Apply thresholding to an image 2.0:
#   - experiment with different threshold values 
#     and see the relation between the threshold value and
#     histogram of the image
#   - set a lower and upper threshold value
#   - make a binary image
# Stretch goals:
# ✓ Explore scikit-image library
# ⁌------------------------------------⁍


import numpy as np
import matplotlib.pyplot as plt
import skimage as ski

# ~~~~~~~~~~~
# Exercise 1.1
# Load the image 'coins.png' with skimage.
# Plot the image.
# Hint: Use skimage.data.coins()

print("\n ~~~~~~~~~~~")
print("Exercise 1.1")

# ..... your code here .....
coins = ski.data.coins()
plt.axis('off')
ski.io.imshow(coins)
plt.show()
# ~~~~~~~~~~~
# Exercise 1.2
# Plot the histogram of the image from Exercise 1.1 for each channel.
# Hint: Use plt.hist().
print("\n ~~~~~~~~~~~")
print("Exercise 1.2")

# ..... your code here .....
plt.title("RGB Coins Histogram")
plt.xlabel("RGB value")
plt.ylabel("Pixel count")
plt.hist(coins.flatten(), bins=256)
print(coins.flatten().shape)
plt.show()
# ~~~~~~~~~~~
# Exercise 1.3
# Experiment with different threshold values applied to different channels.
# Hint: Use np.where().
# The output should be a binary image (black and white).

print("\n ~~~~~~~~~~~")
print("Exercise 1.3")

image = plt.imread("data/cat.jpeg")
threshold = 50
image = image
channel = 0
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
    threshold : int
        The threshold value.
    RGB_channel : int
        The channel to apply the thresholding.

    Returns
    -------
    np.ndarray
        The resulting binary image.
    """
    # ..... your code here .....
    # select channel with index given in input (image[:,:,0])-> will become like a grayscale image
    .....
    # apply threshold as in 1.6 (exercise 3) -> this will create a binary image
    ......
    binary_image = ...
    return binary_image

binary_image = thresholding(image, threshold, channel)
fig, ax = plt.subplots(1, 3, figsize=(10, 5))
for channel in range(0, 3):
    if channel == 0:
        ax[0].imshow(image[:,:,0], cmap="Reds")
    elif channel == 1:
        ax[1].imshow(image[:,:,1], cmap="Greens")
    elif channel == 2:
        ax[2].imshow(image[:,:,2], cmap="Blues")
    else:
        print("This channel does not exist!😡")
        
np.where(image[channel] > threshold, 256, 0)

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
# Exercise 1.4
# Set a lower and upper threshold value.
# Hint: Use np.logical_and().
# The output should be a binary image (black and white).
print("\n ~~~~~~~~~~~")
print("Exercise 1.4")

lower_treshold = ...
upper_treshold = ...
def double_thresholding(
        image: np.ndarray,
        lower_treshold: int,
        upper_treshold: int,
        RGB_channel: int
) -> np.ndarray:
    """A function that binarizes an image based on a lower and upper threshold value
    for a given RGB channel.

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

binary_image = double_thresholding(image, lower_treshold, upper_treshold, channel)

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

