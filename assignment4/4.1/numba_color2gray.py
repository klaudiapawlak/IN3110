import cv2
import time
from numba import njit

def grayscale_filter(filename):

    """
        This function applies the grey-scale filter using Numba.
        Args:
            filename (str): The input image
        Returns:
            grayscale_image (numpy.ndarray): The gray-scale version of the image.
            The grey-scale version of the image as a new jpeg file.
    """

    #start_time = time.time() # start time tracking

    image = cv2.imread(filename)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # switch the channel order

    grayscale_image = grayscale_filter_numba(image) # get the image from grayscale_filter_numba(image) function

    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) # switch back the channel order

    # save a new file with "_grayscale" extension as jpeg
    fn = filename.split(".")
    cv2.imwrite("%s_grayscale.jpeg" %(fn[0]), grayscale_image)

    #print("--- %s seconds ---" % (time.time() - start_time)) # stop time tracking and print out the results

    return grayscale_image

@njit
def grayscale_filter_numba(image):

    """
        Function for applying Numba. Used by grayscale_filter(filename) function.
        Args:
            image (numpy.ndarray): The input image with switched channels.
        Returns:
            grayscale_image (numpy.ndarray): The gray-scale version of the image.
    """

    # apply the filter
    i, j, k = image.shape
    grayscale_image = image
    for x in range(i):
        for y in range(j):
            grayscale_image[x,y] = image[x,y,0]*0.21+image[x,y,1]*0.72+image[x,y,2]*0.07

    return grayscale_image

#grayscale_filter("rain.jpg")
