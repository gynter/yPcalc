#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path

from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup


def fopen(f):
    return open(path.join(path.dirname(__file__), f)).read()


setup(name='yPcalc',
    version='1.0.0',
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
        "Topic :: Utilities",
        "Topic :: System :: Networking",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points='''
    [console_scripts]
    ypcalc = ypcalc:run
    '''
)
