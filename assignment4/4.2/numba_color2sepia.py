import cv2
import time
import numpy as np
from numba import njit

def sepia_filter(filename):

    """
        This function applies the sepia filter using Numba.
        Args:
            filename (str): The input image
        Returns:
            sepia_image (numpy.ndarray): The sepia version of the image.
            The sepia version of the image as a new jpeg file.
    """

    #start_time = time.time() # start time tracking

    image = cv2.imread(filename)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # switch the channel order

    sepia_image = image
    sepia_image = sepia_image.astype("int32") # convert to int32

    # get the image from sepia_filter_numba(image) function
    sepia_image = sepia_filter_numba(image, sepia_image)

    sepia_image = sepia_image.astype("uint8") # convert to uint8
    sepia_image = cv2.cvtColor(sepia_image, cv2.COLOR_RGB2BGR) # switch back the channel order

    # save a new file with "_sepiascale" extension as jpg
    fn = filename.split(".")
    cv2.imwrite("%s_sepiascale.jpeg" %(fn[0]), sepia_image)

    #print("--- %s seconds ---" % (time.time() - start_time)) # stop time tracking and print out the results

    return sepia_image

@njit
def sepia_filter_numba(image, sepia_image):

    """
        Function for applying the filter using Numba. Used by sepia_filter(filename) function.
        Args:
            image (numpy.ndarray): The input image.
        Returns:
            sepia_image (numpy.ndarray): The sepia version of the image.
    """

    # apply the filter
    i, j, k = sepia_image.shape
    for x in range(i):
        for y in range(j):
            sepia_image[x,y,0] = image[x,y,0]*0.393 + image[x,y,1]*0.769 + image[x,y,2]*0.189 #tr
            if sepia_image[x,y,0] > 255:
                sepia_image[x,y,0] = 255
            sepia_image[x,y,1] = image[x,y,0]*0.349+image[x,y,1]*0.686+image[x,y,2]*0.168 #tg
            if sepia_image[x,y,1] > 255:
                sepia_image[x,y,1] = 255
            sepia_image[x,y,2] = image[x,y,0]*0.272+image[x,y,1]*0.534+image[x,y,2]*0.131 #tb
            if sepia_image[x,y,2] > 255:
                sepia_image[x,y,2] = 255
    return sepia_image

#sepia_filter("rain.jpg")
