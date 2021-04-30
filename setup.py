import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
 name="csci-046-data-structures",
 version="1.0.0",
 description="Implementing Multiple Data Structures",
 long_description=README,
 url="https://github.com/DestrosCMC/not_containers/tree/master",
 author="DestrosCMC",
 author_email="kdaly23@cmc.edu",
 license="MIT",
 classifiers=[
     "License :: OSI Approved :: MIT License",
     "Programming Language :: Python :: 3",
     "Programming Language :: Python :: 3.7",
             ],
 packages=["containers"],
 include_package_data=True,
 long_description_content_type='text/markdown',
 install_requires=["pytest", "attrs", "hypothesis"])
