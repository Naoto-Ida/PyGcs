#!/usr/bin/env python

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

setup(
    name="PyGcs",
    version="1.0.0dev",
    packages=["PyGcs"],
    package_dir={"PyGcs": "PyGcs"},
    include_package_data=True,
    url="",
    license="LICENSE.txt",
    description="A Python wrapper for Google Custom Search.",
    author="Naoto Ida",
    zip_safe=False,
)
