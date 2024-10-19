import cv2
import numpy as np

from instapy.gray.python_color2gray import grayscale_filter as py2g
from instapy.gray.numpy_color2gray import grayscale_filter as np2g
from instapy.gray.numba_color2gray import grayscale_filter as nb2g
from instapy.sepia.python_color2sepia import sepia_filter as py2s
from instapy.sepia.numpy_color2sepia import sepia_filter as np2s
from instapy.sepia.numba_color2sepia import sepia_filter as nb2s

def test_grayscalefilter():

    """
        Checks if every functionality of the grey-scale filter works as it should.
    """

    random_image = np.random.randint(255, size=(100, 100, 3)) #3D array with pixel values randomly chosen between 0 and 255

    image = "test_image_gray.jpg"
    cv2.imwrite(image, random_image)
    random_image = cv2.imread(image)

    # apply the filter
    python_grayscale = py2g(image)
    numpy_grayscale = np2g(image)
    numba_grayscale = nb2g(image)

    # random index
    i = np.random.randint(99)
    j = np.random.randint(99)

    py_gray = python_grayscale[i][j]
    np_gray = numpy_grayscale[i][j]
    nb_gray = numba_grayscale[i][j]
    ri_gray = random_image[i][j]

    # apllying the filter manually
    gw = [0.07,0.72,0.21]
    test_gray = int(sum(ri_gray*gw))

    # test
    for k in range(3):
        assert test_gray == py_gray[k] == np_gray[k] == nb_gray[k]

def test_sepiafilter():

    """
        Checks if every functionality of the sepia filter works as it should.
    """

    random_image = np.random.randint(255, size=(100, 100, 3)) #3D array with pixel values randomly chosen between 0 and 255

    image = "test_image_sepia.jpg"
    cv2.imwrite(image, random_image)
    random_image = cv2.imread(image)

    # apply the filter
    python_sepia = py2s(image)
    numpy_sepia = np2s(image)
    numba_sepia = nb2s(image)

    # random index
    i = np.random.randint(99)
    j = np.random.randint(99)

    py_sepia = python_sepia[i][j]
    np_sepia = numpy_sepia[i][j]
    nb_sepia = numba_sepia[i][j]
    ri_sepia = random_image[i][j]

    # apllying the filter manually
    tb = ri_sepia[2]*0.272 + ri_sepia[1]*0.534 + ri_sepia[0]*0.131
    tg = ri_sepia[2]*0.349 + ri_sepia[1]*0.686 + ri_sepia[0]*0.168
    tr = ri_sepia[2]*0.393 + ri_sepia[1]*0.769 + ri_sepia[0]*0.189

    test_sepia = [int(tb), int(tg), int(tr)]
    test_sepia = np.array(test_sepia)
    test_sepia  = np.clip(test_sepia, 0, 255)

    # test
    for k in range(3):
        assert test_sepia[k] == py_sepia[k] == np_sepia[k] == nb_sepia[k]
