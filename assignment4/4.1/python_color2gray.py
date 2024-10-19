import cv2
import time

def grayscale_filter(filename):

    """
        This function applies the gray-scale filter using pure Python.
        Args:
            filename(str) : The input image
        Returns:
            grayscale_image (numpy.ndarray): The gray-scale version of the image.
            The gray-scale version of the image as a new jpeg file.
    """

    #start_time = time.time() # start time tracking

    image = cv2.imread(filename)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # switch the channel order

    # apply the filter
    i, j, k = image.shape
    grayscale_image = image
    for x in range(i):
        for y in range(j):
            grayscale_image[x,y] = image[x,y,0]*0.21 + image[x,y,1]*0.72 + image[x,y,2]*0.07

    grayscale_image = grayscale_image.astype("uint8") # convert the values back to integers
    grayscale_image = cv2.cvtColor(grayscale_image, cv2.COLOR_RGB2BGR) # switch back the channel order

    # save a new file with "_grayscale" extension as jpg
    fn = filename.split(".")
    cv2.imwrite("%s_grayscale.jpeg" %(fn[0]), grayscale_image)

    #print("--- %s seconds ---" % (time.time() - start_time)) # stop time tracking and print out the results

    return grayscale_image

#grayscale_filter("rain.jpg")
