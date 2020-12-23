#!/usr/bin/env python

from setuptools import setup

setup(
    name="unproject_text",
    version="0.1.1",
    description="Perspective recovery of text using transformed ellipses.",
    py_modules=["unproject_text", "ellipse", "moments_from_contour"],
    install_requires=[
        "numpy>=1.1.0",
        "scipy",
        "pillow",
        "matplotlib"
    ],
    entry_points={
        "console_scripts": ["unproject_text=unproject_text:main"]
    },
)
