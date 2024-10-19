import cv2
import time
import numpy as np

def sepia_filter(filename):

    """
        This function applies the sepia filter using Numpy.
        Args:
            filename (str): The input image
        Returns:
            sepia_image (numpy.ndarray): The sepia version of the image.
            The sepia version of the image as a new jpeg file.
    """

    #start_time = time.time() # start time tracking

    image = cv2.imread(filename)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # switch the channel order

    # apply the filter
    sepiamatrix =[[0.393, 0.769, 0.189],
                  [0.349, 0.686, 0.168],
                  [0.272, 0.534, 0.131]]
    sepia_image = np.dot(image,np.transpose(sepiamatrix))
    sepia_image = np.clip(sepia_image,0,255)

    sepia_image = sepia_image.astype("uint8") # convert the values back to integers (uint8)
    sepia_image = cv2.cvtColor(sepia_image, cv2.COLOR_RGB2BGR) # switch the channel order

    # save a new file with "_sepiascale" extension as jpg
    fn = filename.split(".")
    cv2.imwrite("%s_sepiascale2.jpg" %(fn[0]), sepia_image)

    #print("--- %s seconds ---" % (time.time() - start_time)) # stop time tracking and print out the results

    return sepia_image

#sepia_filter("rain.jpg")
