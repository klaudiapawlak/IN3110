import time
from .bin.argumentparser import args

from instapy.gray.python_color2gray import grayscale_filter as py2g
from instapy.gray.numpy_color2gray import grayscale_filter as np2g
from instapy.gray.numba_color2gray import grayscale_filter as nb2g
from instapy.sepia.python_color2sepia import sepia_filter as py2s
from instapy.sepia.numpy_color2sepia import sepia_filter as np2s
from instapy.sepia.numba_color2sepia import sepia_filter as nb2s

input_filename = args.file
sepia = args.sepia
gray = args.gray
scale = args.scale
opacity = args.opacity
output_filename = args.out
implement = args.implement
runtime = args.runtime

def instapy():

    """
        The main function of the instapy package.
        Runs the other functions acordingly.
        Return is based of the choosen implementation method and arguments passed.
    """

    # checks if opacity is between 0 and 1
    if args.opacity>1:
        raise ValueError("The commandline argument passed should be between 0-1 in order to define 0-100% sepia effect.")

    # checks if filter is spesified
    if args.sepia == False and args.gray == False:
        raise ValueError("Filter is not spesified. Use -g for gray or -se for sepia.")

    def grayscale_image(input_filename, output_filename=False):

        """
            The function applies the gray filter acordingly.
            Uses python_color2gray.py, numpy_color2gray.py or numba_color2gray.py.
        """

        if implement == 'python':
            return py2g(input_filename,output_filename,scale)
        elif implement == 'numpy':
            return np2g(input_filename,output_filename,scale)
        elif implement == 'numba':
            return nb2g(input_filename,output_filename,scale)

    def sepia_image(input_filename, output_filename=False):

        """
            The function applies the sepia filter acordingly.
            Uses python_color2sepia.py, numpy_color2sepia.py or numba_color2sepia.py.
        """

        if implement == 'python':
            return py2s(input_filename,output_filename,scale,opacity)
        elif implement == 'numpy':
            return np2s(input_filename,output_filename,scale,opacity)
        elif implement == 'numba':
            return nb2s(input_filename,output_filename,scale,opacity)

    # tracks the runtime
    if runtime:
        if gray:
            start_time = time.time()
            grayscale_image(input_filename, output_filename)
            grayscale_image(input_filename, output_filename)
            grayscale_image(input_filename, output_filename)
            run_time = (time.time()-start_time)/3
            print(("Average time over 3 runs: %f seconds." %(run_time)))
        if sepia:
            start_time = time.time()
            sepia_image(input_filename, output_filename)
            sepia_image(input_filename, output_filename)
            sepia_image(input_filename, output_filename)
            run_time = (time.time()-start_time)/3
            print(("Average time over 3 runs: %f seconds." %(run_time)))
    else:
        if gray:
            return grayscale_image(input_filename, output_filename)
        elif sepia:
            return sepia_image(input_filename, output_filename)
