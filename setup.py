#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools


# get version info
def _get_version():
    with open("nerf/__init__.py", encoding="utf-8") as init_file:
        for line in init_file:
            if line.startswith("__version__"):
                version_info = {}
                exec(line, version_info)
                return version_info["__version__"]
    raise ValueError("version number is missing!")


with open("README.md", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='nerfpy',
    description=(
        "NeRFpy: A Python implementation and"
        " extension of Natural Extension Reference Frame."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    version=_get_version(),
    url='https://github.com/smu-tao-group/nerfpy',
    author='Hao Tian',
    author_email='htian1997@gmail.com',
    license='Apache License 2.0',
    packages=setuptools.find_packages(),
    install_requires=["numpy"],
    package_data={'nerf': ['data/*']},
    python_requires='>=3.7'
)
