#!/usr/bin/env python
from __future__ import print_function

import os
import sys
from setuptools import setup


if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    os.system("python setup.py bdist_wheel upload")
    print("You probably want to also tag the version now:")
    print("  git tag -a VERSION -m 'version VERSION'")
    print("  git push --tags")
    sys.exit()

setup(
    name="unproject_text",
    version="0.1.1",
    author="Matt Zucker",
    description="Perspective recovery of text using transformed ellipses.",
    url="https://github.com/mzucker/unproject_text",
    packages=setuptools.find_packages(),
    py_modules=["unproject_text"],
    install_requires=[
        "numpy>=1.1.0",
        "scipy",
        "pillow",
        "matplotlib"
    ],
    entry_points="""
        [console_scripts]
        unproject_text=unproject_text:main
    """,
)
