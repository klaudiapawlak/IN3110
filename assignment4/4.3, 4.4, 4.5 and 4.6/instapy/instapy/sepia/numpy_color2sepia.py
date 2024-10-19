import cv2
import numpy as np

def sepia_filter(input_filename, output_filename=False, scale=False, opacity=1):

    """
        This function applies the sepia filter using Numpy.
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

    o = opacity

    # apply the filter
    sepiamatrix =[[0.393+0.607*(1-o), 0.769-0.769*(1-o), 0.189-0.189*(1-o)],
                  [0.349-0.349*(1-o), 0.686+0.314*(1-o), 0.168-0.168*(1-o)],
                  [0.272-0.272*(1-o), 0.534-0.534*(1-o), 0.131+0.869*(1-o)]]

    sepia_image = np.dot(image,np.transpose(sepiamatrix))
    sepia_image = np.clip(sepia_image,0,255)

    sepia_image = sepia_image.astype("uint8") # convert the values back to uint8
    sepia_image = cv2.cvtColor(sepia_image, cv2.COLOR_RGB2BGR) # switch the channel order

    if output_filename:
        # save a new file with given name as jpeg
        cv2.imwrite("%s.jpeg" %(output_filename), sepia_image)

    return sepia_image
