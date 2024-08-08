import numpy as np
import matplotlib.pyplot as plt
import skimage as ski
import tifffile as tif
from tqdm import tqdm

#first, I will import the video (the derotated image) (using tifffile)
video = tif.imread('/Users/training/Downloads/derotated/derotated.tif')
print(np.shape(video))
#afterwards, I will define FOUR functions, A, B and C:

#FUNCTION A: at each frame, i.e. identifying a lower and higher threshold 
#based on the histogram of a given image (this I think increases the noise but makes the image sharper)
def single_thresholding_for_each_image( #defining the function
        video, contrast_level): #assigning two inputs to the function
    for number in tqdm(range(0, 8258)): #creating a for loop to iterate the thresholds to each frame
        t_min, t_max = find_thresholds(video[number, :, :], contrast_level) #assigning the min and max threshold values to a variable
        first_thresholded_video = np.where(video[number, :, :] < t_min, 0, video[number, :, :]) #adding the lower threshold to the video
        second_thresholded_video= np.where(first_thresholded_video > t_max, 256, first_thresholded_video) #adding the upper threshold to the video
    return second_thresholded_video #assigning an output which is the new created video
    
"""This function will apply two unique thresholds to each frame of a video
and return a new thresholded video ()
...............
"""

#FUNCTION B: or all the video, i.e. identifying the two thresholds based on the overall histogram.
def double_thresholding_for_whole_video(
        video, contrast_level):
    t_min, t_max = find_thresholds(video, contrast_level)
    first_thresholded_video = np.where(video < t_min, 0, video)
    second_thresholded_video = np.where(first_thresholded_video > t_max, 256, first_thresholded_video)
    return second_thresholded_video
"""This function will apply two thresholds to a single video (first_thresholded_video)
and return a new video (second_thresholded_video)

    Parameters
    ----------
    video : np.ndarray
        The input video.
    contrast_level : int
        The input contrast level
 
    Returns
    -------
    second_thresholded_video
        The new output video.
"""

#FUNCTION C:
def find_thresholds(
        array, contrast_level):
    t_min, t_max = np.percentile(
        array, (contrast_level, 100 - contrast_level)
    )

    return t_min, t_max
"""This function will identify two thresholds based on an input array and contrast level
and return the two threshold values (t_min, t_max) 

    Parameters
    ----------
    array : np.ndarray
        The input video.
    contrast_level : int
        The input contrast level
 
    Returns
    -------
    t_min, t_max
        The new output thresholds.
"""

#After, use the two functions to generate two different videos with different contrasts
video_contrast_single = single_thresholding_for_each_image(video, 0.9)
video_contrast_double = double_thresholding_for_whole_video(video, 0.9)

#Contrast is needed to improve image registration quality and so the cells can be viewed in better detail

#However contrast increases noise in the images therefore after creating the two functions, I will apply 
#the different contrast methodologies to the video and compare

#i want to save these new videos to files
tif.imwrite('resulting_video_1.tif', video_contrast_single)
tif.imwrite('resulting_video_2.tif', video_contrast_double)