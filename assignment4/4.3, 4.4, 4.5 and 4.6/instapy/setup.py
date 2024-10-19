import setuptools

setuptools.setup(
    name='instapy',
    version='1.0',
    author='klaudiap',
    packages=setuptools.find_packages(),
    entry_points ={'console_scripts': ['instapy = instapy.main:instapy']},
    setup_requires=['numpy', 'setuptools>=18.0'],
    install_requires=['numpy', 'numba', 'opencv-python'],
    python_requires='>=3.6'
)
