import cv2
import time

def grayscale_filter(input_filename, output_filename=False, scale=False):

    """
        This function applies the grey-scale filter using pure Python.
        Required args:
            input_filename (str): The input image
        Optional args:
            output_filename (str): The output image (will be saved as jpeg)
            scale (float): Scale factor
        Returns:
            grayscale_image (numpy.ndarray): The gray-scale version of the image.
            The grey-scale version of the image as a new jpeg file (if output_filename is provided).
    """

    #start_time = time.time() # start time tracking

    image = cv2.imread(input_filename)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # switch the channel order

    # scale the image
    if scale:
        image = cv2.resize(image, (0, 0), fx=scale, fy=scale)

    # apply the filter
    i, j, k = image.shape
    grayscale_image = image
    for x in range(i):
        for y in range(j):
            grayscale_image[x,y] = image[x,y,0]*0.21 + image[x,y,1]*0.72 + image[x,y,2]*0.07

    grayscale_image = grayscale_image.astype("uint8") # convert the values back to integers
    grayscale_image = cv2.cvtColor(grayscale_image, cv2.COLOR_RGB2BGR) # switch back the channel order

    if output_filename:
        # save a new file with given name as jpeg
        cv2.imwrite("%s.jpeg" %(output_filename), grayscale_image)

    #print("--- %s seconds ---" % (time.time() - start_time)) # stop time tracking and print out the results

    return grayscale_image

#grayscale_filter("rain.jpg")
