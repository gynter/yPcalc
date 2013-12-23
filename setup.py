#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path

from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup


def fopen(f):
    return open(path.join(path.dirname(__file__), f)).read()


setup(name='yPcalc',
    version='0.1.0-beta.2',
    description='An IPv4 and IPv6 subnet calculator.',
    long_description=fopen("README.md"),
    keywords=['ipv4', 'ipv6', 'subnet', 'calculator', 'network'],
    license=fopen("LICENSE.md"),
    url='https://github.com/gynter/yPcalc',
    author='Günter Kits',
    author_email='gynter@kits.ee',
    maintainer='Günter Kits',
    maintainer_email='gynter@kits.ee',
    packages=['ypcalc'],
    package_dir={'': 'src'},
    requires=['ipcalc'],
    provides=['yPcalc'],
    platforms=['all'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "Topic :: Games/Entertainment :: First Person Shooters",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "License :: OSI Approved :: MIT License",
        "License :: Other/Proprietary License",
    ],
    entry_points='''
    [console_scripts]
    ypcalc = ypcalc:run
    '''
)
