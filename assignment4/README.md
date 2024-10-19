# README.md Assignment4

## Table of contents

### 4.1
* [python_color2gray.py](#python_color2graypy)
* [python_report_color2gray.txt](https://github.uio.no/IN3110/IN3110-klaudiap/blob/master/assignment4/4.1/python_report_color2gray.txt)
* [numpy_color2gray.py](#numpy_color2graypy)
* [numpy_report_color2gray.txt](https://github.uio.no/IN3110/IN3110-klaudiap/blob/master/assignment4/4.1/numpy_report_color2gray.txt)
* [numba_color2gray.py](#numba_color2graypy)
* [numba_report_color2gray.txt](https://github.uio.no/IN3110/IN3110-klaudiap/blob/master/assignment4/4.1/numba_report_color2gray.txt)
### 4.2
* [python_color2sepia.py](#python_color2sepiapy)
* [python_report_color2sepia.txt](https://github.uio.no/IN3110/IN3110-klaudiap/blob/master/assignment4/4.2/python_report_color2sepia.txt)
* [numpy_color2sepia.py](#numpy_color2sepiapy)
* [numpy_report_color2sepia.txt](https://github.uio.no/IN3110/IN3110-klaudiap/blob/master/assignment4/4.2/numpy_report_color2sepia.txt)
* [numba_color2sepia.py](#numba_color2sepiapy)
* [numba_report_color2sepia.txt](https://github.uio.no/IN3110/IN3110-klaudiap/blob/master/assignment4/4.2/numba_report_color2sepia.txt)
### 4.3, 4.4, 4.5 and 4.6
* [instapy](#instapy)
 ```
instapy  
  │───setup.py
  │
  └───instapy
      │   main.py
      │   __init__.py
      │
      ├───bin
      │       argumentparser.py
      │       __init__.py
      │
      ├───gray
      │       numba_color2gray.py
      │       numpy_color2gray.py
      │       python_color2gray.py
      │       __init__.py
      │
      ├───sepia
      │       numba_color2sepia.py
      │       numpy_color2sepia.py
      │       python_color2sepia.py
      │       __init__.py
      │
      └───test
              test_instapy.py
              __init__.py
 ```


## python_color2gray.py

### Prerequisites
- Python 3
- OpenCV
- time

### Functionality
This function applies the gray (black and white) filter using pure Python. It creates a new file with *_greyscale* extension as an jpeg. Read the reports to see the time differences compared to other methods.

### Usage
***greyscale_filter(filename)*** function needs one argument provided by the user:
- **filename (str)**: The input image.
E.g. if your file name was rain (jpeg) you could use:
 ``` 
 1. import python_color2gray as py2g
 2. py2g.grayscale_filter("rain.jpeg")
 ```
 
## numpy_color2gray.py

### Prerequisites
- Python 3
- OpenCV
- Numpy
- time

### Functionality
This function applies the gray (black and white) filter using Numpy. It creates a new file with *_greyscale* extension as an jpeg. Read the reports to see the time differences compared to other methods.

### Usage
***greyscale_filter(filename)*** function needs one argument provided by the user:
- **filename (str)**: The input image.
E.g. if your file name was rain (jpeg) you could use:
 ``` 
 1. import numpy_color2gray as np2g
 2. np2g.grayscale_filter("rain.jpeg")
 ``` 
 
## numba_color2gray.py

### Prerequisites
- Python 3
- OpenCV
- Numba
- time

### Functionality
This function applies the gray (black and white) filter using Numba. It creates a new file with *_greyscale* extension as an jpeg. Read the reports to see the time differences compared to other methods.

### Usage
***greyscale_filter(filename)*** function needs one argument provided by the user:
- **filename (str)**: The input image.
E.g. if your file name was rain (jpeg) you could use:
 ``` 
 1. import numba_color2gray as nb2g
 2. nb2g.grayscale_filter("rain.jpeg")
 ``` 
 
## python_color2sepia.py

### Prerequisites

- Python 3
- OpenCV
- time

### Functionality

This function applies the sepia filter using pure Python. It creates a new file with *_sepiascale* extension as an jpeg. Read the reports to see the time differences compared to other methods.

### Usage

***sepia_filter(filename)*** function needs one argument provided by the user:
- **filename (str)**: The input image.

E.g. if your file name was rain (jpeg) you could use:
 ``` 
 1. import python_color2sepia as py2s
 2. py2s.sepia_filter("rain.jpeg")
 ```
## numpy_color2sepia.py

### Prerequisites

- Python 3
- OpenCV
- Numpy
- time

### Functionality

This function applies the sepia filter using Numpy. It creates a new file with *_sepiascale* extension as an jpeg. Read the reports to see the time differences compared to other methods.

### Usage

***sepia_filter(filename)*** function needs one argument provided by the user:
- **filename (str)**: The input image.

E.g. if your file name was rain (jpeg) you could use:
 ``` 
 1. import numpy_color2sepia as np2s
 2. np2s.sepia_filter("rain.jpeg")
 ``` 

## numba_color2sepia.py

### Prerequisites

- Python 3
- OpenCV
- Numba
- time

### Functionality

This function applies the sepia filter using Numba. It creates a new file with *_sepiascale* extension as an jpeg. Read the reports to see the time differences compared to other methods.

### Usage

***sepia_filter(filename)*** function needs one argument provided by the user:
- **filename (str)**: The input image.

E.g. if your file name was rain (jpeg) you could use:
 ``` 
 1. import numba_color2sepia as nb2s
 2. nb2s.sepia_filter("rain.jpeg")
 ``` 
 
## instapy

### Prerequisites

- Python 3
- Pytest
- Setuptools
- Numpy
- Numba

### Installation

To install the package use pip install, e.g.:

 ``` 
 $ pip install instapy
 ``` 

### Functionality

This package applies the sepia or the grayscale filter on the image using one of the methods listed below:
- Python
- Numpy
- Numba

It returns a ***numpy.ndarray (the output image)***. If an output filename is provided it creates a new jpeg file with a selected filter. It can also resize the image as long as the scale factor is given. The instapy filter lets you chose the opacity of the sepia filter (if wanted). This filter can also track the average time of 3 runs with the selected method. 

### Usage

Use  ```-h ``` to get the list of the cmd arguments for this package. The input filename and filter method are required arguments. The rest of the arguments are optional.

   ``` 

  -h, --help                                                   Show this help message and exit
  -f FILE, --file FILE                                         The filename of file to apply filter to (str).
  -se, --sepia                                                 Select sepia filter
  -g, --gray                                                   Select gray filter
  -sc SCALE, --scale SCALE                                     Scale factor to resize image (float). Is 1 by default.
  -op OPACITY, --opacity OPACITY                               Set opacity from 0 to 1 (float). Is 1 by default.
  -o OUT, --out OUT                                            The output filename (str)
  -i {python,numba,numpy}, --implement {python,numba,numpy}    Choose the implementation. Numba is default.
  -r, --runtime                                                Average time of 3 runs.
  
   ``` 
  
  For example for applying the filter on rain.jpg with the numpy method, 0.8 opacity and the output filename rain_grayscale.jpeg you can use:
  
   ``` 
   $ instapy -f rain.jpg -o rain_grayscale.jpeg -se -op 0.8 -i numpy -r
   ``` 
   

 ### Test
 
 These tests checks if every functionality of the instapy.py works as it should. For running the test, go to *test* directory (instapy/instapy/test) and use:
 
 ```
 $ pytest
 ```
 
 ### Note 1
 
 This package is similar to what I delivered a year ago.
