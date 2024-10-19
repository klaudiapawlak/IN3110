import cv2
import time
import numpy as np


def grayscale_filter(filename):

    """
        This function applies the gray-scale filter using numpy.
        Args:
            filename (str): The input image
        Returns:
            grayscale_image (numpy.ndarray): The gray-scale version of the image.
            The grey-scale version of the image as a new jpeg file.
    """

    #start_time = time.time() # start time tracking

    image = cv2.imread(filename)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # switch the channel order

    grayscale_image = image
    grayscale_image = grayscale_image.astype("int32") # convert to int32 (for calculation)

    # apply the filter
    w = [0.21,0.72,0.07]
    for i in range(3):
        grayscale_image[:,:,i] = np.dot(image, w)


    grayscale_image = grayscale_image.astype("uint8") # convert the values back to uint8
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) # switch back the channel order

    # save a new file with "_grayscale" extension as jpeg
    fn = filename.split(".")
    cv2.imwrite("%s_grayscale.jpeg" %(fn[0]), grayscale_image)

    #print("--- %s seconds ---" % (time.time() - start_time)) # stop time tracking and print out the results

    return grayscale_image

#grayscale_filter("rain.jpg")
