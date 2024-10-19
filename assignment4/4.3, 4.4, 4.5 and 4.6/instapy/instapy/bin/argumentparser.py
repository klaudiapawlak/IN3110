import argparse

parser = argparse.ArgumentParser(description="Instapy")
parser.add_argument('-f', '--file', required=True, help='The filename of file to apply filter to.')
parser.add_argument('-se', '--sepia', action='store_true', default=False, help='Select sepia filter')
parser.add_argument('-g', '--gray', action='store_true', default=False, help='Select gray filter')
parser.add_argument('-sc', '--scale', default=1.0, type=float, help='Scale factor to resize image')
parser.add_argument('-op', '--opacity', default=1, type=float, help='Set opacity.')
parser.add_argument('-o', '--out', default=False, help='The output filename')
parser.add_argument('-i', '--implement', default='numba',choices=['python', 'numba', 'numpy'], help='Choose the implementation')
parser.add_argument('-r', '--runtime', action='store_true', help='Average time of 3 runs.')
args = parser.parse_args()
