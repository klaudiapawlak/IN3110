import cv2
import time

def sepia_filter(filename):

    """
        This function applies the sepia filter using pure Python.
        Args:
            filename (str): The input image
        Returns:
            sepia_image (numpy.ndarray): The sepia version of the image.
            The sepia version of the image as a new jpg file.
    """

    #start_time = time.time() # start time tracking

    image = cv2.imread(filename)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # switch the channel order

    # apply the filter
    sepia_image = image
    sepia_image = sepia_image.astype("int32") # convert to int32 (for calculation)

    i, j, k = image.shape
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

    sepia_image = sepia_image.astype("uint8") # convert back to uint8
    sepia_image = cv2.cvtColor(sepia_image, cv2.COLOR_RGB2BGR) # switch the channel order

    # save a new file with "_sepiascale" extension as jpg
    fn = filename.split(".")
    cv2.imwrite("%s_sepiascale.jpg" %(fn[0]), sepia_image)

    #print("--- %s seconds ---" % (time.time() - start_time)) # stop time tracking and print out the results

    return sepia_image

#sepia_filter("rain.jpg")
