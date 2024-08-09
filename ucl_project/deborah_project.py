import numpy as np
import matplotlib.pyplot as plt
import skimage as ski
import tifffile as tif
from tqdm import tqdm

#first, I will import the video (the derotated video clip) (using tifffile)
video = tif.imread('/Users/training/Downloads/derotated/derotated.tif')
#then, I will express all non-variable integer values using the variable 'video'
frame_range = int(np.arange(video.shape[0] + 1)[-1])
t_min_value = int(np.min(video))
t_max_value = int(np.max(video))
#afterwards, I will define THREE functions, A, B and C:
#FUNCTION A: at each frame, i.e. identifying a lower and higher threshold based on the histogram of a given image 
#(this I think increases the noise but makes the image sharper)
def single_thresholding_for_each_image( #defining the function
        video: np.ndarray, 
        contrast_level: int
) -> np.ndarray: #assigning two inputs to the function
    """This function will apply two unique thresholds to each frame of a video
    and return a new thresholded video (arr)

    Parameters
    ----------
    video : np.ndarray
        The input video.
    contrast_level : int
        The input contrast level

    Returns
    -------
    arr : np.ndarray
        The new output video.
    """
    arr = []
    for number in tqdm(range(frame_range)): #creating a 'for loop' to iterate the thresholds to each frame
        t_min, t_max = find_thresholds(video[number, :, :], contrast_level) #assigning the min. and max. threshold values to two variables
        first_thresholded_image = np.where(video[number, :, :] < t_min, t_min_value, video[number, :, :]) #adding the lower threshold to the frame
        second_thresholded_image= np.where(first_thresholded_image > t_max, t_max_value, first_thresholded_image) #adding the upper threshold to the frame
        arr.append(second_thresholded_image) #add each thresholded frame to the list, one after the other
    return np.asarray(arr) #assigning an output which is the new created video
#FUNCTION B: or all the video, i.e. identifying the two thresholds based on the overall histogram.
def double_thresholding_for_whole_video(
        video: np.ndarray, 
        contrast_level: int
) -> np.ndarray:
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
    second_thresholded_video : np.ndarray
        The new output video.
    """
    t_min, t_max = find_thresholds(video, contrast_level)
    first_thresholded_video = np.where(video < t_min, t_min_value, video)
    second_thresholded_video = np.where(first_thresholded_video > t_max, t_max_value, first_thresholded_video)
    return second_thresholded_video

#FUNCTION C:
def find_thresholds(
        array: np.ndarray,
        contrast_level: int
) -> np.ndarray:
    """This function will identify two thresholds based on an input array and contrast level
    and return the two threshold values (t_min, t_max) 

    Parameters
    ----------
    array : np.ndarray
        The input video/image.
    contrast_level : int
        The input contrast level

    Returns
    -------
    t_min, t_max : int
        The new output thresholds.
    """
    t_min, t_max = np.percentile(array, (contrast_level, 100 - contrast_level))
    return t_min, t_max

#After, use the two functions to generate two different videos with different contrasts
video_contrast_single = single_thresholding_for_each_image(video, 0.35)
video_contrast_double = double_thresholding_for_whole_video(video, 0.35)

#Contrast is needed to improve image registration quality and so the cells can be viewed in better detail

#However contrast increases noise in the images therefore after creating the two functions, I will apply 
#the different contrast methodologies to the video and compare

#i want to save these new videos to files
tif.imwrite('resulting_video_1.tif', video_contrast_single)
tif.imwrite('resulting_video_2.tif', video_contrast_double)
