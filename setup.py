#!/usr/bin/env python
import os
import re

from setuptools import setup, find_packages


ROOT = os.path.dirname(__file__)
VERSION_RE = re.compile(r'''__version__ = ['"]([0-9.]+)['"]''')


def get_version():
    init = open(os.path.join(ROOT, 'awspricing', '__init__.py')).read()
    return VERSION_RE.search(init).group(1)


setup(
    name='awspricing',
    version=get_version(),
    description='An SDK for AWS Pricing',
    long_description=open('README.rst').read(),
    author='Garrett Heel',
    url='https://github.com/lyft/awspricing',
    packages=find_packages(exclude=['tests*']),
    install_requires=[
        'requests>=2.5.0,<3.0.0',    # License: Apache2
        'six>=1.0.0,<2.0.0',         # License: MIT
    ],
    extras_require={':python_version=="2.7"': ['typing>=3.5.0.0,<3.6.0.0']},
    license="apache2",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
