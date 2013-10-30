#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


setup(name='yPcalc',
      version='0.1-beta.1',
      description='An IPv4 and IPv6 subnet calculator',
      long_description='An IPv4 and IPv6 subnet calculator',
      keywords=['ipv4', 'ipv6', 'subnet', 'calculator', 'network'],
      license='MIT License (Expat)',
      url='https://github.com/gynter/yPcalc',
      author='Günter Kits',
      author_email='gynter@kits.ee',
      maintainer='Günter Kits',
      maintainer_email='gynter@kits.ee',
      packages=['ypcalc'],
      package_dir={'': 'src'},
      requires=['ipcalc'],
      provides=['yPcalc', 'ipcalc'],
      platforms=['all'],
      entry_points='''
      [console_scripts]
      ypcalc = ypcalc:run
      '''
)
