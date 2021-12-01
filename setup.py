"""
Setup file and install script for GDBIGtools.

Version 1.1.4 (Nov 30, 2021)
Copyright (c) 2021 Chengrui Wang
"""
import os
from argparse import Namespace

try:
    from setuptools import setup, find_packages

    _has_setuptools = True
except ImportError:
    from distutils.core import setup, find_packages

DESCRIPTION = "GDBIGtools: A command line tools for GDBIG variant browser."

meta = Namespace(
    __DISTNAME__="GDBIGtools",
    __AUTHOR__="Chengrui Wang",
    __AUTHOR_EMAIL__="aiyacharley@outlook.com",
    __URL__="https://github.com/aiyacharley/GDBIGtools",
    __LICENSE__="BSD (3-clause)",
    __DOWNLOAD_URL__="https://github.com/aiyacharley/GDBIGtools",
    __VERSION__="1.1.4",
)

if __name__ == "__main__":

    THIS_PATH = os.path.abspath(os.path.dirname(__file__))
    long_description = os.path.join(THIS_PATH, "README.md")

    setup(name=meta.__DISTNAME__,
          version=meta.__VERSION__,
          author=meta.__AUTHOR__,
          author_email=meta.__AUTHOR_EMAIL__,
          maintainer=meta.__AUTHOR__,
          maintainer_email=meta.__AUTHOR_EMAIL__,
          description=DESCRIPTION,
          long_description=(open(long_description).read()),
          long_description_content_type="text/markdown",
          license=meta.__LICENSE__,
          url=meta.__URL__,
          download_url=meta.__URL__,
          packages=find_packages(),
          include_package_data=True,
          install_requires=[
              "PyYAML>=5.1.2",
              "requests>=2.22.0",
              "click"
          ],
          entry_points={
              "console_scripts": [
                  "GDBIGtools = GDBIGtools.GDBIGtools:GDBIGtools"
              ]
          },
          classifiers=[
              "Intended Audience :: Science/Research",
              "Programming Language :: Python :: 3.6",
              "Programming Language :: Python :: 3.7",
              "Programming Language :: Python :: 3.8",
              "License :: OSI Approved :: BSD License",
              "Topic :: Scientific/Engineering :: Bio-Informatics",
              "Operating System :: POSIX",
              "Operating System :: POSIX :: Linux",
              "Operating System :: MacOS"],
          )
