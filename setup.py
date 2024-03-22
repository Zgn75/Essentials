from setuptools import setup, find_packages

AUTHOR = 'Zgn'
VERSION = '1.0.0' 
DESCRIPTION = 'A package that covers essential functions for you'
LONG_DESCRIPTION = 'Discover a comprehensive package designed to encompass all the essential functions you need, tailored specifically to streamline your daily tasks and enhance your efficiency effortlessly.'
NAME = 'Essentials'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name=NAME, 
        version=VERSION,
        author=AUTHOR,
        author_email="zgnbusinesses@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=["essentials"], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'essentials'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)