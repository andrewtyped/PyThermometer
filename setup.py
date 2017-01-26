"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

setup(
    name='PyThermometer',

    version='0.0.1',

    description='A module for reading temperatures from a file and reporting them to the web',

    author="Andrew S Barger",
    author_email='asbarg01@gmail.com',

    license="MIT",

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: IoT developers',
        'Topic :: Software Development :: IoT',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=['requests'],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'temp_reporter=temp_reporter:main',
        ],
    },
)