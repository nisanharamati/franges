import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "franges",
    version = "1.0.1",
    author = "Nisan Haramati",
    author_email = "hanisan@gmail.com",
    description = ("Franges adds support for floating point and fixed precision (Decimal) range generator functions."),
    license = "LGPLv3+",
    maintainer = "Nisan Haramati",
    url = "https://github.com/nisanharamati/franges",
    packages=['franges',],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries',
    ],
)
