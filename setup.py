# -*- coding: utf-8 -*-

# Copyright 2016 tsuru authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
from setuptools import setup, find_packages

setup(
    name="tsuru-sphinx",
    url="https://github.com/tsuru/tsuru-sphinx",
    version='0.1.3',
    description="Sphinx extensions used in tsuru documentation",
    author="Tsuru",
    author_email="tsuru@corp.globo.com",
    classifiers=[
        "Programming Language :: Python :: 2.7",
    ],
    packages=find_packages(exclude=["docs", "tests"]),
    include_package_data=True,
    install_requires=[
        "docutils==0.12",
        "PyYAML==3.11",
    ],
    entry_points={
        'console_scripts': [
            'tsuru_sphinx=tsuru_sphinx:main',
        ],
    },
)
