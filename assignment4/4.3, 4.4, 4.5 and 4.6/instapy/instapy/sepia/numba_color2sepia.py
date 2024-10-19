import cv2
import numpy as np
from numba import njit

def sepia_filter(input_filename, output_filename=False, scale=False, opacity=1):

    """
        This function applies the sepia filter using Numba.
        Required args:
            input_filename (str): The input image
        Optional args:
            output_filename (str): The output image (will be saved as jpeg)
            scale (float): Scale factor
            opacity (float): Opacity of the sepia filter from 0 to 1
        Returns:
            sepia_image (numpy.ndarray): The sepia version of the image.
            The sepia version of the image as a new jpeg file (if output_filename is provided).
    """

    image = cv2.imread(input_filename)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # switch the channel order

    # scale the image
    if scale:
        image = cv2.resize(image, (0, 0), fx=scale, fy=scale)

    sepia_image = image
    sepia_image = sepia_image.astype("int32") # convert to int32

    # get the image from sepia_filter_numba(image) function
    sepia_image = sepia_filter_numba(image, sepia_image, opacity)

    sepia_image = sepia_image.astype("uint8") # convert to uint8
    sepia_image = cv2.cvtColor(sepia_image, cv2.COLOR_RGB2BGR) # switch back the channel order

    if output_filename:
        # save a new file with given name as jpeg
        cv2.imwrite("%s.jpeg" %(output_filename), sepia_image)

    return sepia_image

@njit
def sepia_filter_numba(image, sepia_image, opacity):

    """
        Function for applying the filter using Numba. Used by sepia_filter(input_filename) function.
        Args:
            image (numpy.ndarray): The input image.
            opacity (float): Opacity of the sepia filter from 0 to 1 (default = 1)
        Returns:
            sepia_image (numpy.ndarray): The sepia version of the image.
    """

    # apply the filter
    o = opacity
    i, j, k = sepia_image.shape
    for x in range(i):
        for y in range(j):
            sepia_image[x,y,0] = image[x,y,0]*(0.393+0.607*(1-o)) + image[x,y,1]*(0.769-0.769*(1-o)) + image[x,y,2]*(0.189-0.189*(1-o)) #tr
            if sepia_image[x,y,0] > 255:
                sepia_image[x,y,0] = 255
            sepia_image[x,y,1] = image[x,y,0]*(0.349-0.349*(1-o)) + image[x,y,1]*(0.686+0.314*(1-o)) + image[x,y,2]*(0.168-0.168*(1-o)) #tg
            if sepia_image[x,y,1] > 255:
                sepia_image[x,y,1] = 255
            sepia_image[x,y,2] = image[x,y,0]*(0.272-0.272*(1-o)) + image[x,y,1]*(0.534-0.534*(1-o)) + image[x,y,2]*(0.131+0.869*(1-o)) #tb
            if sepia_image[x,y,2] > 255:
                sepia_image[x,y,2] = 255
    return sepia_image
